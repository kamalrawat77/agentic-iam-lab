import json

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from scripts.config import get_gemini_key, MODEL_NAME
from scripts.core.plan import Plan, PlanStep
from scripts.core.planner_schema import PlannerResponse
from scripts.core.status import InvestigationStatus
from scripts.tools.validator import validate


class Planner:

    def __init__(self, registry):
        self.registry = registry

        self.parser = PydanticOutputParser(
            pydantic_object=PlannerResponse
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are an IAM Investigation Planner.

                Create an investigation plan only.
                Never execute tools or answer the investigation question.

                Use only tools listed in the supplied tool catalogue.
                Use the exact registered tool names.
                Return the response in the required schema format.

                {format_instructions}
                """
            ),
            (
                "human",
                """
                Investigation question:
                {question}

                Available tools:
                {available_tools}
                """
            ),
        ])

        self.model = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            google_api_key=get_gemini_key(),
            temperature=0,
        )

        self.chain = self.prompt | self.model | self.parser

    def create_plan(self, investigation):
        available_tools = self.registry.list_for_planner()

        # Step 1: Ask the model for a schema-conforming response.
        planner_output = self.chain.invoke({
            "question": investigation.question,
            "available_tools": json.dumps(
                available_tools,
                indent=2
            ),
            "format_instructions":
                self.parser.get_format_instructions(),
        })

        # Step 2: Validate each proposed tool and its arguments.
        steps = []

        for proposed_step in planner_output.steps:
            tool = self.registry.get(proposed_step.tool)

            if tool is None:
                raise ValueError(
                    f"Planner returned unknown tool: "
                    f"{proposed_step.tool}"
                )

            try:
                validate(tool, proposed_step.arguments)
            except Exception as exc:
                raise ValueError(
                    f"Invalid arguments for tool "
                    f"'{proposed_step.tool}': {exc}"
                ) from exc

            steps.append(
                PlanStep(
                    tool=proposed_step.tool,
                    purpose=proposed_step.purpose,
                    description=proposed_step.description,
                    arguments=proposed_step.arguments,
                )
            )

        # Step 3: Mutate the investigation only after validation passes.
        investigation.plan = Plan(
            goal=planner_output.investigation,
            steps=steps,
        )

        investigation.status = InvestigationStatus.PLANNED

        return investigation
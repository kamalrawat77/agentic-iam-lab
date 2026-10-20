import json

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from scripts.config import get_gemini_key, MODEL_NAME
from scripts.core.plan import PlanStep, Plan
from scripts.core.status import InvestigationStatus


class Planner:

    def __init__(self, registry):
        self.registry = registry

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are an IAM Investigation Planner.

                Create an investigation plan only.
                Never answer the user's question.

                Use only tools listed in the user message.
                Return a JSON object with these keys:
                - investigation: a string describing the goal
                - steps: a list of plan steps

                Each step must contain:
                - tool: registered tool name
                - purpose: why the tool is needed
                - description: what it should do
                - arguments: a JSON object of tool arguments

                Do not include markdown fences.
                """
            ),
            (
                "human",
                """
                Question:
                {question}

                Available tools:
                {available_tools}
                """
            )
        ])

        self.model = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            google_api_key=get_gemini_key(),
            temperature=0,
        )

        self.parser = JsonOutputParser()

        # LCEL: connect prompt, model, and parser.
        self.chain = self.prompt | self.model | self.parser

    def create_plan(self, investigation):
        available_tools = self.registry.list_for_planner()

        planner_output = self.chain.invoke({
            "question": investigation.question,
            "available_tools": json.dumps(
                available_tools,
                indent=2
            ),
        })

        # Validate the basic response shape before building domain objects.
        if not isinstance(planner_output, dict):
            raise ValueError("Planner output must be a JSON object.")

        if not isinstance(planner_output.get("steps"), list):
            raise ValueError("Planner output must contain a steps list.")

        steps = []

        for step in planner_output["steps"]:
            if not isinstance(step, dict):
                raise ValueError("Each plan step must be a JSON object.")

            arguments = step.get("arguments", {})

            if not isinstance(arguments, dict):
                raise ValueError(
                    "Each plan step's arguments must be a JSON object."
                )

            steps.append(
                PlanStep(
                    tool=step["tool"],
                    purpose=step["purpose"],
                    description=step["description"],
                    arguments=arguments,
                )
            )

        investigation.plan = Plan(
            goal=planner_output["investigation"],
            steps=steps,
        )

        investigation.status = InvestigationStatus.PLANNED

        return investigation
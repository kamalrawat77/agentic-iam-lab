import json
from google import genai
from scripts.config import (
    get_gemini_key,
    MODEL_NAME
)
from scripts.core.plan import (PlanStep,Plan)
from scripts.core.status import InvestigationStatus

client = genai.Client(api_key=get_gemini_key())


class Planner:

    def __init__(self, registry):
        self.client = genai.Client(api_key=get_gemini_key())
        self.registry = registry

    def create_plan(self, investigation):
        available_tools = self.registry.list_for_planner()
        prompt = f"""
You are an IAM Investigation Planner.

Question:
{investigation.question}

Available Tools:
{json.dumps(available_tools, indent=2)}

Your task is ONLY to create an investigation plan.

Never answer the user's question.

Return JSON ONLY.

Format:

Return ONLY JSON in this format:

{{
    "investigation":"...",
    "steps":[
        {{
            "tool":"dormant_accounts",
            "purpose":"...",
            "description":"Find dormant accounts",
            "parameters":{{
                "days":{{
                    "type":"integer",
                    "default":90
                }}
            }}
          }}
        ]
}}
"""

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        planner_output = json.loads(text)
        steps = []
        for step in planner_output["steps"]:
            steps.append(

                PlanStep(

                    tool=step["tool"],

                    purpose=step["purpose"],

                    description=step["description"],

                    arguments={}
                )
            )

        investigation.plan = Plan(

            goal=planner_output["investigation"],

            steps=steps
        )



        investigation.status = InvestigationStatus.PLANNED

        return investigation

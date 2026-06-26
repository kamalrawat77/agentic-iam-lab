import json
from google import genai
from scripts.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

client = genai.Client(api_key=GEMINI_API_KEY)


class Planner:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def create_plan(self, question, available_tools):
        prompt = f"""
You are an IAM Investigation Planner.

Question:
{question}

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
            "tool":"trend_analysis",
            "purpose":"..."
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

        return json.loads(text)

import json
import time
from pydantic import ValidationError
from google import genai

from core.config import Config
from schemas.dsa_schema import DSAResponse


class AIService:
    def __init__(self, config: Config, logger):
        self.Config = config
        self.logger = logger

        if not self.Config.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not set in environment variables.")

        self.client = genai.Client(api_key=self.Config.GEMINI_API_KEY)

    def _build_prompt(self, problem_text: str) -> str:
        return f"""
You are a senior Data Structures and Algorithms instructor.

Respond ONLY in valid JSON.
No markdown.
No backticks.
No explanation outside JSON.

Return EXACTLY this structure:

{{
  "title": "",
  "topic": "",
  "difficulty": "Easy | Medium | Hard",
  "approach": "",
  "code": "",
  "time_complexity": "",
  "space_complexity": ""
}}

Rules:
- Standalone Python function
- Snake_case function name
- Explanation inside docstring
- Difficulty must be exactly Easy, Medium, or Hard

Problem:
{problem_text}
"""

    def generate_solution(self, problem_text: str) -> DSAResponse:
        prompt = self._build_prompt(problem_text)

        for attempt in range(1, self.Config.MAX_RETRIES + 1):
            try:
                self.logger.info(f"AI request attempt {attempt}")

                response = self.client.models.generate_content(
                    model=self.Config.MODEL_NAME,
                    contents=prompt,
                    config={
                        "temperature": 0,
                        "response_mime_type": "application/json"
                    }
                )

                raw_text = response.text.strip()

                # Gemini sometimes wraps JSON in markdown
                if raw_text.startswith("```"):
                    raw_text = raw_text.split("```")[1].strip()

                # self.logger.info(f"Raw Gemini response:\n{raw_text}")

                parsed_json = json.loads(raw_text)

                validated_response = DSAResponse(**parsed_json)

                self.logger.info("AI response successfully validated.")
                return validated_response

            except (json.JSONDecodeError, ValidationError) as e:
                self.logger.error(f"Validation error on attempt {attempt}: {e}")

            except Exception as e:
                self.logger.error(f"Unexpected error on attempt {attempt}: {e}")

            sleep_time = 2 ** attempt
            self.logger.info(f"Retrying after {sleep_time} seconds...")
            time.sleep(sleep_time)

        raise RuntimeError("AI generation failed after maximum retry attempts.")

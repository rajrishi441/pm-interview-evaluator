import os
import json
import re
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Create client
client = genai.Client(api_key=API_KEY)


CLASSIFICATION_PROMPT = """
You are an interview evaluation engine.

Classify the following answer into ONE of these categories:

- behavioral
- motivation
- introduction
- product_design
- unclear

Return ONLY valid JSON in this format:

{
  "answer_type": "...",
  "confidence": 0.0-1.0,
  "reasoning": "short explanation"
}

Answer:
"""


STAR_SCORING_PROMPT = """
You are a senior product management interviewer.

Evaluate the following behavioral interview answer using the STAR framework.

Score each category from 0 to 20.

Categories:
- Situation Clarity
- Task Clarity
- Action Depth
- Result & Quantification
- Leadership Signals

Return ONLY valid JSON in this format:

{
  "situation_score": 0-20,
  "task_score": 0-20,
  "action_score": 0-20,
  "result_score": 0-20,
  "leadership_score": 0-20,
  "total_score": 0-100,
  "strengths": "short paragraph",
  "improvements": "short paragraph",
  "missing_elements": ["list of missing components"]
}

Answer:
"""


def clean_json_response(text):
    cleaned = re.sub(r"```json|```", "", text).strip()
    return cleaned


def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


def classify_answer(transcript):
    raw_text = generate_response(CLASSIFICATION_PROMPT + transcript)
    cleaned_text = clean_json_response(raw_text)

    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw_text
        }


def score_behavioral_answer(transcript):
    raw_text = generate_response(STAR_SCORING_PROMPT + transcript)
    cleaned_text = clean_json_response(raw_text)

    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw_text
        }

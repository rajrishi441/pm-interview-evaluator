from llm_engine import run_structured_prompt

QUESTION_EXTRACTION_PROMPT = """
You are an expert interview conversation analyzer.

Given a full transcript of an interview:

1. Identify all interviewer questions.
2. Detect main questions and group their follow-up questions.
3. Follow-up questions are those that dig deeper into the same topic.
4. Ignore small talk and introductions.
5. Do NOT invent or rephrase questions.
6. Extract only what appears in the transcript.
7. If no clear follow-ups exist, return an empty list for followups.

Return ONLY valid JSON in this format:

[
  {
    "main_question": "...",
    "followups": ["...", "..."]
  }
]

Transcript:
"""


def extract_questions(transcript):
    return run_structured_prompt(QUESTION_EXTRACTION_PROMPT + transcript)
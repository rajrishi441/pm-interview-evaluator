from llm_engine import run_structured_prompt

QA_HIERARCHICAL_PROMPT = """
You are an expert interview conversation analyzer.

Given a full interview transcript:

1. Identify main interviewer questions (new topics).
2. Identify follow-up questions that probe deeper into the SAME topic.
3. Group follow-ups under the correct main question.
4. Extract the candidate answer corresponding to each question.
5. Ignore greetings and small talk.
6. Do NOT invent content.

Return ONLY valid JSON in this format:

[
  {
    "main_question": "...",
    "main_answer": "...",
    "followups": [
        {
            "question": "...",
            "answer": "..."
        }
    ]
  }
]

Transcript:
"""


def segment_hierarchical_qa(transcript,api_key):
    return run_structured_prompt(QA_HIERARCHICAL_PROMPT + transcript,api_key)
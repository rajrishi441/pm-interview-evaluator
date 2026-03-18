from llm_engine import run_structured_prompt

QUESTION_TYPE_PROMPT = """
You are an expert Product Management interview classifier.

Classify the given interview question into ONE of the following categories:

- behavioral
- product_design
- estimation
- rca
- strategy
- unclear

Definitions:

behavioral:
Questions about past experiences, leadership, conflict, motivation.

product_design:
Design or improve a product, define users, features, metrics.

estimation:
Guesstimate, market sizing, numerical approximations.

rca:
Root cause analysis, debugging a metric drop, diagnosing issues.

strategy:
Market entry, monetization, business model, competitive positioning.

unclear:
If the question does not clearly fit any category.

Return ONLY valid JSON in this format:

{
  "question_type": "...",
  "confidence": 0.0-1.0,
  "reasoning": "short explanation"
}

Question:
"""


def classify_question_type(question_text,api_key):
    return run_structured_prompt(QUESTION_TYPE_PROMPT + question_text , api_key)
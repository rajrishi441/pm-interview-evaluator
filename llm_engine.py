import os
import json
import re
from dotenv import load_dotenv
from google import genai

def get_client(api_key):
    if not api_key:
        raise ValueError("API key is required.")
    return genai.Client(api_key=api_key)


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

PRODUCT_DESIGN_PROMPT = """
You are a senior product management interviewer.

Evaluate the following Product Design interview answer.

Score each category from 0 to 20.

Evaluation Criteria:

1. User Empathy & Segmentation
   - Did the candidate clearly define target users?
   - Did they narrow to a specific persona?

2. Problem Identification
   - Did they identify real user pain points before jumping to solutions?

3. Structured Thinking
   - Did they use a logical framework?
   - Clarify -> Context -> Users -> Pain Points -> Solutions -> Prioritization -> Metrics

4. Solution Quality & Feasibility
   - Are solutions creative yet practical?
   - Are they buildable?

5. Metrics Definition
   - Did they define North Star Metric?
   - Did they include success metrics and guardrails?

Return ONLY valid JSON:

{
  "user_empathy_score": 0-20,
  "problem_identification_score": 0-20,
  "structure_score": 0-20,
  "solution_quality_score": 0-20,
  "metrics_score": 0-20,
  "total_score": 0-100,
  "strengths": "short paragraph",
  "improvements": "short paragraph",
  "missing_elements": ["list"]
}

Answer:
"""


ESTIMATION_PROMPT = """
You are a senior product management interviewer.

Evaluate the following Estimation (Guesstimate) interview answer.

Score each category from 0 to 20.

Evaluation Criteria:

1. Clarifying Questions
   - Did the candidate narrow scope properly?
   - Did they clarify assumptions?

2. Equation Structure
   - Did they define a clear formula before plugging numbers?

3. Assumption Quality
   - Were assumptions realistic and stated clearly?

4. Sanity Checking
   - Did they validate the final number?

5. Calculation Flow & Accuracy
   - Was the logic sequential?
   - Were calculations reasonable?

Return ONLY valid JSON:

{
  "clarification_score": 0-20,
  "equation_structure_score": 0-20,
  "assumption_score": 0-20,
  "sanity_check_score": 0-20,
  "calculation_score": 0-20,
  "total_score": 0-100,
  "strengths": "short paragraph",
  "improvements": "short paragraph",
  "missing_elements": ["list"]
}

Answer:
"""
RCA_PROMPT = """
You are a senior product management interviewer.

Evaluate the following Root Cause Analysis (RCA) interview answer.

Score each category from 0 to 20.

Evaluation Criteria:

1. Hypothesis Breadth
   - Did the candidate consider multiple possible causes?
   - Internal + external factors?

2. Structured Debugging
   - Did they logically narrow down hypotheses?
   - Use stepwise elimination?

3. Metric Awareness
   - Did they reference relevant metrics?
   - Funnel breakdown? Leading vs lagging indicators?

4. Context Awareness
   - Platform differences?
   - Regional or payment issues?
   - External events?

5. Prioritization & Actionability
   - Did they define which issue to test first?
   - Clear next steps?

Return ONLY valid JSON:

{
  "hypothesis_score": 0-20,
  "structure_score": 0-20,
  "metric_score": 0-20,
  "context_score": 0-20,
  "actionability_score": 0-20,
  "total_score": 0-100,
  "strengths": "short paragraph",
  "improvements": "short paragraph",
  "missing_elements": ["list"]
}

Answer:
"""

STRATEGY_PROMPT = """
You are a senior product management interviewer.

Evaluate the following Product Strategy interview answer.

Score each category from 0 to 20.

Evaluation Criteria:

1. Market Sizing & Opportunity
   - Did the candidate estimate TAM/SAM/SOM?
   - Did they assess opportunity size?

2. Competitive Landscape
   - Did they identify key competitors?
   - Did they differentiate positioning?

3. Business Model & Unit Economics
   - Did they discuss revenue model?
   - CAC vs LTV?
   - Cost structure?

4. Strategic Fit
   - Does this align with company vision?
   - Does it leverage existing strengths?

5. Risk Assessment & Trade-offs
   - Did they mention risks?
   - Operational challenges?
   - Regulatory or execution constraints?

Return ONLY valid JSON:

{
  "market_score": 0-20,
  "competition_score": 0-20,
  "economics_score": 0-20,
  "strategic_fit_score": 0-20,
  "risk_score": 0-20,
  "total_score": 0-100,
  "strengths": "short paragraph",
  "improvements": "short paragraph",
  "missing_elements": ["list"]
}

Answer:
"""

def clean_json_response(text):
    cleaned = re.sub(r"```json|```", "", text).strip()
    return cleaned


def generate_response(prompt, api_key):
    client = get_client(api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return getattr(response, "text", "")

def run_structured_prompt(prompt, api_key):
    raw_text = generate_response(prompt, api_key)
    cleaned_text = clean_json_response(raw_text)

    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw_text
        }


def classify_answer(transcript, api_key):
    return run_structured_prompt(CLASSIFICATION_PROMPT + transcript, api_key)


def score_behavioral_answer(transcript, api_key):
    return run_structured_prompt(STAR_SCORING_PROMPT + transcript, api_key)

def score_product_design_answer(transcript, api_key):
    return run_structured_prompt(PRODUCT_DESIGN_PROMPT + transcript, api_key)

def score_estimation_answer(transcript, api_key):
    return run_structured_prompt(ESTIMATION_PROMPT + transcript, api_key)

def score_rca_answer(transcript, api_key):
    return run_structured_prompt(RCA_PROMPT + transcript, api_key)

def score_strategy_answer(transcript, api_key):
    return run_structured_prompt(STRATEGY_PROMPT + transcript, api_key)

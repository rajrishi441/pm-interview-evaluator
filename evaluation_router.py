from question_classifier import classify_question_type
from llm_engine import score_behavioral_answer

# Placeholder evaluators (to be implemented later)
def evaluate_product_design(transcript):
    return {"note": "Product design evaluator not implemented yet"}

def evaluate_estimation(transcript):
    return {"note": "Estimation evaluator not implemented yet"}

def evaluate_rca(transcript):
    return {"note": "RCA evaluator not implemented yet"}

def evaluate_strategy(transcript):
    return {"note": "Strategy evaluator not implemented yet"}


def route_evaluation(question_text, transcript):
    classification = classify_question_type(question_text)

    if "error" in classification:
        return {
            "question": question_text,
            "error": "Classification failed",
            "details": classification
        }

    question_type = classification.get("question_type")

    if question_type == "behavioral":
        evaluation = score_behavioral_answer(transcript)

    elif question_type == "product_design":
        evaluation = evaluate_product_design(transcript)

    elif question_type == "estimation":
        evaluation = evaluate_estimation(transcript)

    elif question_type == "rca":
        evaluation = evaluate_rca(transcript)

    elif question_type == "strategy":
        evaluation = evaluate_strategy(transcript)

    else:
        evaluation = {"note": "Unclear question type"}

    return {
        "question": question_text,
        "question_type": question_type,
        "evaluation": evaluation
    }
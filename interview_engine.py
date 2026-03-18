from speaker_identifier import identify_speakers
from qa_segmenter import segment_hierarchical_qa
from question_classifier import classify_question_type

from llm_engine import (
    score_behavioral_answer,
    score_product_design_answer,
    score_estimation_answer,
    score_rca_answer,
    score_strategy_answer
)


def route_evaluation(question_type, answer, api_key):
    if question_type == "behavioral":
        return score_behavioral_answer(answer, api_key)
    elif question_type == "product_design":
        return score_product_design_answer(answer, api_key)
    elif question_type == "estimation":
        return score_estimation_answer(answer, api_key)
    elif question_type == "rca":
        return score_rca_answer(answer, api_key)
    elif question_type == "strategy":
        return score_strategy_answer(answer, api_key)
    else:
        return {
            "error": "Unsupported question type"
        }


def evaluate_full_transcript(transcript, api_key, interviewee_name=None):

    # Step 1: Speaker Detection
    speaker_map = identify_speakers(transcript,api_key, interviewee_name)

    # Step 2: Convert speaker map back to structured text
    reconstructed_transcript = ""
    for line in speaker_map:
        reconstructed_transcript += f"{line['speaker'].upper()}: {line['text']}\n"

    # Step 3: Hierarchical Segmentation
    qa_tree = segment_hierarchical_qa(reconstructed_transcript,api_key)

    results = []

    # Step 4: Per Main Question Evaluation
    for block in qa_tree:
        question = block["main_question"]
        answer = block["main_answer"]

        question_type_data = classify_question_type(question,api_key)
        question_type = question_type_data.get("question_type")

        evaluation = route_evaluation(question_type, answer, api_key)

        results.append({
            "question": question,
            "question_type": question_type,
            "answer" : answer,
            "evaluation": evaluation
        })

    return results
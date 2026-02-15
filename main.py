import sys
import os
import json
import subprocess

from extract_audio import extract_audio
from llm_engine import classify_answer, score_behavioral_answer


def transcribe_audio(audio_path):
    """
    Uses Whisper CLI to transcribe audio.
    Returns transcript as string.
    """
    command = [
        "whisper",
        audio_path,
        "--model", "base",
        "--output_format", "txt"
    ]

    subprocess.run(command, check=True)

    transcript_file = audio_path.replace(".wav", ".txt")

    if not os.path.exists(transcript_file):
        raise FileNotFoundError("Transcript file not generated.")

    with open(transcript_file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <video_path>")
        sys.exit(1)

    video_path = sys.argv[1]

    if not os.path.exists(video_path):
        print("Video file not found.")
        sys.exit(1)

    audio_output = "temp_audio.wav"

    print("\nExtracting audio...")
    extract_audio(video_path, audio_output)

    print("Transcribing audio...")
    transcript = transcribe_audio(audio_output)

    print("\nClassifying answer...")
    classification = classify_answer(transcript)
    print(classification)

    # 🔵 Create structured result container
    final_result = {
        "answer_type": classification.get("answer_type"),
        "confidence": classification.get("confidence"),
        "classification_reasoning": classification.get("reasoning"),
        "star_analysis": None
    }

    if classification.get("answer_type") == "behavioral":
        print("\nScoring behavioral answer...")
        star_score = score_behavioral_answer(transcript)
        print(star_score)
        final_result["star_analysis"] = star_score
    else:
        print("\nNot a behavioral answer. Skipping STAR scoring.")

    # 🔵 Save JSON result
    with open("analysis_result.json", "w") as f:
        json.dump(final_result, f, indent=4)

    print("\nAnalysis saved to analysis_result.json")



if __name__ == "__main__":
    main()

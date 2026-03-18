import sys
import os
import json
import subprocess
import argparse

from extract_audio import extract_audio
from interview_engine import evaluate_full_transcript #classify_answer, score_behavioral_answer


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
    # if len(sys.argv) < 2:
        # print("Usage: python main.py <video_path>")
        # sys.exit(1)

    # video_path = sys.argv[1]
    parser = argparse.ArgumentParser(description="PM Interview Analyzer")

    parser.add_argument("video_path", help="Path to video file")
    parser.add_argument("--api_key", required=True, help="API key for LLM")
    parser.add_argument("--interviewee_name", default=None, help="Name of candidate")

    args = parser.parse_args()

    video_path = args.video_path
    api_key = args.api_key
    interviewee_name = args.interviewee_name

    if not os.path.exists(video_path):
        print("Video file not found.")
        sys.exit(1)

    audio_output = "temp_audio.wav"

    print("\nExtracting audio...")
    extract_audio(video_path, audio_output)

    print("Transcribing audio...")
    transcript = transcribe_audio(audio_output)

    print("\nEvaluating full interview...")
    result = evaluate_full_transcript(transcript,api_key,interviewee_name)
    with open("analysis_result.json", "w") as f:
        json.dump(result, f, indent=4)
    print("\nAnalysis saved to analysis_result.json")
   

if __name__ == "__main__":
    main()

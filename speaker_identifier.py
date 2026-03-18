from llm_engine import run_structured_prompt

SPEAKER_IDENTIFICATION_PROMPT = """
You are an expert interview conversation analyzer.

Some lines may start with:
[FORCED_INTERVIEWER]

Those lines MUST be labeled as interviewer.

For remaining lines:
- Maintain logical alternation.
- The candidate gives longer explanations.
- The interviewer asks questions.
- Keep consistency.
- Do NOT override forced labels.

Return ONLY valid JSON:

[
  {
    "speaker": "interviewer" or "candidate",
    "text": "exact line"
  }
]

Transcript:
"""

def apply_speaker_constraints(transcript, interviewee_name=None):
    lines = [line.strip() for line in transcript.split("\n") if line.strip()]
    
    constrained = []
    
    for i, line in enumerate(lines):
        if i == 0:
            constrained.append(f"[FORCED_INTERVIEWER] {line}")
        elif interviewee_name and interviewee_name.lower() in line.lower():
            constrained.append(f"[FORCED_INTERVIEWER] {line}")
        else:
            constrained.append(line)
    
    return "\n".join(constrained)

def identify_speakers(transcript, api_key   ,interviewee_name=None):
    processed_transcript = apply_speaker_constraints(transcript,interviewee_name)
    return run_structured_prompt(SPEAKER_IDENTIFICATION_PROMPT + processed_transcript,api_key)
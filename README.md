=======
# PM Interview Performance Evaluator (AI-Powered)

## Overview

This project analyzes interview videos and generates structured, actionable feedback using AI.

It processes full interview recordings and evaluates candidate performance across:

* Verbal answer quality (STAR framework)
* Question type classification
* Structured strengths and improvement insights

---

## Problem Statement

Interview preparation is often subjective and manual.

Candidates struggle with:

* Identifying weak answers
* Structuring responses effectively
* Getting consistent, objective feedback

This tool solves that by:

* Automatically analyzing interview recordings
* Applying structured evaluation frameworks
* Providing clear, actionable feedback

---

## End-to-End Pipeline

```text
Video
→ Audio Extraction (FFmpeg)
→ Transcription (Whisper)
→ Speaker Detection (LLM)
→ Question Segmentation
→ Question Classification
→ Answer Evaluation (STAR-based)
→ JSON Output
```

---

## Sample Interview Video

Due to file size limitations, the sample interview video is hosted externally:

[https://drive.google.com/file/d/1BwDNmxesxh2cCI5ojedC40y6opMNlw0Y/view?usp=sharing]

---

## Features

* Extracts audio from video files
* Transcribes speech using Whisper
* Identifies interviewer vs candidate
* Detects and segments interview questions
* Classifies question types (behavioral, product, etc.)
* Evaluates answers using STAR framework
* Generates structured JSON output

---

## Setup Instructions

### 1. Install Python (3.10+)

### 2. Install FFmpeg

Required for audio extraction and Whisper transcription.

### 3. Clone the Repository

```bash
git clone https://github.com/rajrishi441/pm-interview-evaluator.git
cd pm-interview-evaluator
```

### 4. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Add API Key

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key_here
```

---

## How to Run

```bash
python main.py sample_video.mp4 --api_key "YOUR_API_KEY" --interviewee_name "Raj"
```

### Output

analysis_result.json

---

## Sample Output

```json
[
  {
    "question": "Tell me about a time you handled stakeholder conflict.",
    "question_type": "behavioral",
    "evaluation": {
      "total_score": 33,
      "strengths": "...",
      "improvements": "...",
      "missing_elements": [
        "Lack of context",
        "Missing structured explanation",
        "Weak action breakdown"
      ]
    }
  }
]
```

---

## Project Structure

* main.py → Entry point (CLI + pipeline orchestration)
* extract_audio.py → Extracts audio from video
* interview_engine.py → Core evaluation logic
* qa_segmenter.py → Segments questions and answers
* question_classifier.py → Classifies question type
* speaker_identifier.py → Identifies speakers
* llm_engine.py → Handles LLM-based scoring
* evaluation_router.py → Routes scoring logic

---

## Limitations

* Transcription accuracy depends on audio quality
* Speaker detection may not be perfect in noisy environments
* Currently focuses only on verbal evaluation
* No body language or facial analysis yet

---

## Future Improvements

* UI
* Speech metrics (WPM, filler words, pauses)
* Improved segmentation accuracy
* Interview performance dashboard
* Real-time mock interview feedback
* Multi-round interview tracking

---

## Author

Raj Rishi

---

## Why This Project Matters

This project demonstrates:

* End-to-end AI system design
* Real-world problem solving
* Integration of multiple AI components
* Product thinking combined with technical execution
>>>>>>> 5fa94f2 (Full pipeline upgrade: video processing, Whisper transcription, LLM-based interview evaluation, CLI support, improved README)

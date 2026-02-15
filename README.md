# PM Interview Behavioral Evaluator (MVP v1)

## Overview

This project evaluates a single interview answer from a video file.

Pipeline:
Video → Audio → Whisper Transcription → Gemini Classification → STAR Scoring → JSON Output

Currently supports:
- Behavioral answer detection
- STAR framework scoring
- Structured JSON output

---

## Setup

### 1. Install Python 3.10+

### 2. Install FFmpeg
Required for MoviePy and Whisper.

### 3. Clone the repo

git clone <your-repo-url>
cd pm_interview_dashboard

### 4. Create virtual environment

python -m venv venv
venv\Scripts\activate  (Windows)

### 5. Install dependencies

pip install -r requirements.txt

### 6. Add Gemini API key

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here

---

## Usage

python main.py sample_video.mp4

Output:
analysis_result.json

---

## Architecture

main.py → Orchestrates flow  
extract_audio.py → Extracts audio from video  
llm_engine.py → Handles Gemini classification & scoring  

---

## Phase 2 (Planned)

- Multi-answer segmentation
- Full interview analysis
- Dashboard UI
- Improved scoring heuristics

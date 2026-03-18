# PM Interview Performance Evaluator (AI-Powered)

## Overview

This project analyzes interview videos and generates structured, actionable feedback using AI.

It processes full interview recordings and evaluates candidate performance across:

* Verbal answer quality (STAR framework)
* Question type classification
* Structured strengths and improvement insights

---

## Problem Statement

Interview preparation for Product Managers is often subjective and manual.

Candidates struggle with:

* Identifying weak answers
* Structuring responses effectively
* Getting consistent, objective feedback

This tool solves that by:

* Automatically analyzing interview recordings
* Applying structured evaluation frameworks
* Providing clear, actionable feedback

---

## Supported PM Interview Types

This system is specifically designed for Product Manager (PM) interview preparation.

It automatically detects and evaluates different types of PM interview questions:

### 1. Behavioral Interviews

Evaluated using the STAR framework:

* Situation
* Task
* Action
* Result
* Leadership signals

---

### 2. Product Design Interviews

* User segmentation and persona clarity
* Problem identification before solutioning
* Structured thinking approach
* Solution feasibility
* Metrics definition (North Star + success metrics)

---

### 3. Estimation (Guesstimates)

* Clarifying questions
* Equation setup
* Assumptions
* Sanity checks
* Logical calculation flow

---

### 4. Root Cause Analysis (RCA)

* Hypothesis generation
* Structured debugging
* Metric awareness
* Context analysis
* Actionable next steps

---

### 5. Product Strategy

* Market sizing
* Competitive analysis
* Business model & unit economics
* Strategic alignment
* Risk assessment

---

### 6. Introduction / Motivation

* Classified but not deeply scored in the current version

---

## How Evaluation Works

1. Detects question boundaries from transcript
2. Classifies each question type
3. Routes answers to the appropriate evaluation framework
4. Generates structured scores and feedback

Each answer is evaluated using frameworks similar to real PM interviews at top companies.

---

## End-to-End Pipeline

```text
Video
→ Audio Extraction (FFmpeg)
→ Transcription (Whisper)
→ Speaker Detection (LLM)
→ Question Segmentation
→ Question Classification
→ Answer Evaluation (Framework-based)
→ JSON Output
```

---

## Sample Interview Video

Due to file size limitations, the sample interview video is hosted externally:

https://drive.google.com/file/d/1BwDNmxesxh2cCI5ojedC40y6opMNlw0Y/view?usp=sharing

---

## Features

* Extracts audio from video files
* Transcribes speech using Whisper
* Identifies interviewer vs candidate
* Detects and segments interview questions
* Classifies question types (behavioral, product, etc.)
* Evaluates answers using structured frameworks
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

---

### 4. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

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

## Sample Output against the sample video

```json
[
    {
        "question": "Okay. So, in today's scenario, I want you to imagine that we're working at Flipkart. And we're noticing that there's a decline of about 15% of cart additions to the additions to the shopping cart in the last three days. Can you help us diagnose the issue?",
        "question_type": "rca",
        "answer": "Sure. So, Stephen, before I jump into sort of finding out what the problem is, I just want to understand what do we define as cart additions here so that we are on the same page? Sure. Also, Flipkart has both website and mobile app. So, are we looking at a generic 15% decline? Or has it been observed only on the mobile app or the website? Okay. Sure. So, I will just speak two minutes to sort of make my framework and think about Flipkart in general and we'll then share the framework with you. Okay. Yeah. Okay. I'm ready. So, Stephen, our first question is the cart additions that we're measuring. So, it's sort of like a metric which might be measured using some analytics tool. So, have we checked whether this analytics tool was working well over the last three days? Okay. So, now that we have all of that answered, I will just share deeply my outline of the framework that I'm going to follow, to where I have the root cause. So, first, I will look at the external factors which will involve, which will involve getting information on what competitors have done in the last few days. Has there been any product launch or has it been any new announcement, which might have taken away certain customer fees or certain sort of, which might have taken away certain customer fees from Flipkart? Second, we look at the demographic feature. So, has it affected any particular customer segment or any particular demographic feature or that particular customer segment? Third, we look at the macroeconomic feature, macroeconomic changes. So, has there been any news or any seasonality impact or any kind of pattern in the external factors, which might impact the overall purchasing behavior? So, what are the internal changes that we have done? So, have we made any updates in the mobile app, have we made any design changes, etc. And then, will be the overall journey of the user on the mobile app, because we are...",
        "evaluation": {
            "hypothesis_score": 16,
            "structure_score": 14,
            "metric_score": 15,
            "context_score": 18,
            "actionability_score": 8,
            "total_score": 71,
            "strengths": "The candidate started strong with excellent clarifying questions, demonstrating an immediate grasp of critical details like metric definition and platform specificity. They also showed good discipline by outlining a structured framework and prioritizing data integrity checks (analytics tool). Their consideration of both internal (product changes) and a wide range of external factors (competitors, demographics, macroeconomic, seasonality) indicates a holistic understanding of potential root causes.",
            "improvements": "The candidate could improve by explicitly detailing how they would prioritize investigation areas once their initial data integrity checks are complete, rather than just listing them. More specific examples of metrics (e.g., conversion rates at different funnel stages, traffic sources) and how they would use these to narrow down hypotheses would strengthen the 'Structured Debugging' and 'Metric Awareness' scores. The answer also ended abruptly, leaving the 'user journey' part incomplete.",
            "missing_elements": [
                "Explicit prioritization criteria for hypotheses (e.g., impact, effort, likelihood) beyond the initial data check.",
                "Detailed breakdown of the user funnel beyond a general mention of the 'overall journey'.",
                "Specific examples of metrics to track within each hypothesis area (e.g., pricing changes, promotions, inventory levels, page load times).",
                "A clear 'next steps' action plan after identifying potential root causes (e.g., A/B testing, deeper dives, stakeholder communication).",
                "Consideration of technical issues beyond just the analytics tool (e.g., backend errors, API failures, payment gateway issues)."
            ]
        }
    }
]
```

---

## Project Structure

* main.py → Entry point (CLI + orchestration)
* extract_audio.py → Audio extraction
* interview_engine.py → Core evaluation pipeline
* qa_segmenter.py → Q/A segmentation
* question_classifier.py → Question classification
* speaker_identifier.py → Speaker detection
* llm_engine.py → LLM-based scoring
* evaluation_router.py → Routing logic

---

## Limitations

* Transcription accuracy depends on audio quality
* Speaker detection may not be perfect in noisy environments
* Currently focuses only on verbal evaluation
* No body language or facial analysis

---

## Future Improvements

* Speech metrics (WPM, filler words, pauses)
* Improved segmentation accuracy
* Interview performance dashboard
* Real-time mock interview mode
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

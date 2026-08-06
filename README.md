# 🤖 AI Product Analyst Agent

An LLM-powered product analysis assistant that automatically analyzes customer feedback and generates actionable product insights.

This project demonstrates how Large Language Models can support product teams by transforming unstructured user feedback into structured issue analysis, prioritization, and improvement recommendations.

---

## 🎯 Project Overview

Product teams receive large amounts of customer feedback every day, including bug reports, usability complaints, service issues, and pricing concerns.

Manually analyzing this feedback is time-consuming and difficult to scale.

This project builds an AI Product Analyst Agent that can:

- Identify the main user issue
- Categorize feedback types
- Evaluate severity and priority
- Generate actionable product recommendations

The goal is to simulate how AI assistants can support product managers in customer insight analysis and decision-making.

---

## ✨ Key Features

### 1. Customer Feedback Analysis

Users can input natural language feedback, and the agent automatically extracts:

- Issue summary
- Problem category
- Severity level
- Priority level
- Recommended actions


### 2. LLM-powered Product Reasoning

The agent uses an LLM API to perform:

- User pain point identification
- Root cause hypothesis generation
- Product impact assessment
- Action recommendation


### 3. Interactive Product Demo

A Streamlit-based interface allows users to:

- Submit customer feedback
- Generate AI-powered product insights
- View structured recommendations instantly


---

## 🏗️ System Architecture


User Feedback

↓

Streamlit Web Interface

↓

LLM Agent (DeepSeek API)

↓

Product Insight Generation

↓

Issue Classification & Action Recommendation


---

## 🛠️ Tech Stack

### Programming

- Python

### AI / LLM

- DeepSeek API
- Prompt Engineering
- LLM-based reasoning

### Data & Product

- Pandas
- Structured text analysis

### Application

- Streamlit


---

## 📸 Demo


Example input:

> "The app crashes every time I upload photos."


Generated insight:

- Category: Functional Bug
- Severity: Critical
- Priority: P1
- Recommended actions:
  - Investigate crash logs
  - Identify root cause
  - Implement regression testing


---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone <your-repository-url>
cd AI_Product_Analyst_Agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
```bash
Create a .env file:
DEEPSEEK_API_KEY=your_api_key
```

### 4. Run application
```bash
streamlit run app.py
```

## 💡 Product Value
This project explores the application of AI agents in product management workflows.
Potential use cases:
Customer feedback analysis
Product issue triage
User research assistance
Feature prioritization support

## 👤 Author
Nicky Chen

Interests:
AI Product Management
Data Analytics
Machine Learning
Natural Language Processing

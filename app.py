import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def analyze_feedback(feedback):

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role":"system",
                "content":
                """
You are an AI Product Analyst.

Analyze customer feedback.

Return:

Issue:
Category:
Severity:
Priority:
Recommended Action:

"""
            },
            {
                "role":"user",
                "content":feedback
            }
        ]
    )

    return response.choices[0].message.content



st.title("🤖 AI Product Analyst Agent")

st.write(
"""
Analyze customer feedback and generate product insights automatically.
"""
)


feedback = st.text_area(
    "Enter customer feedback:"
)


if st.button("Analyze"):

    if feedback:

        result = analyze_feedback(feedback)

        st.subheader("Product Insight")

        st.write(result)

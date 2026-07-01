import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_product(text):
    prompt = f"""
    You are a food safety expert.

    Analyze these product ingredients:

    {text}

    Return ONLY valid JSON in this format:

    {{
        "category": "",
        "health_score": "",
        "risk_level": "",
        "pros": [],
        "cons": [],
        "recommendation": "",
        "alternatives": []
    }}

    Do not return markdown.
    Do not use ```json.
    Return only JSON.
    """

    response = model.generate_content(prompt)

    cleaned = response.text.strip()

    # Safety: Gemini kabhi kabhi markdown me bhej deta hai
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by Gemini",
            "raw_response": cleaned
        }
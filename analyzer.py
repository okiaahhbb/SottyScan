from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

def get_client():
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    return Groq(api_key=api_key)

def analyze_news(text):
    client = get_client()
    prompt = f"""
তুমি একজন বাংলাদেশের expert fact-checker।
নিচের বাংলা নিউজটি বিশ্লেষণ করো।

নিউজ: {text}

শুধুমাত্র এই EXACT format এ উত্তর দাও:
VERDICT: [সত্যি অথবা মিথ্যা অথবা সন্দেহজনক]
CONFIDENCE: [শুধু সংখ্যা, যেমন 85]
কারণ: [২-৩ লাইনে বাংলায়]
EMOTION: [ভয় অথবা রাগ অথবা ধর্মীয় উস্কানি অথবা দেশপ্রেম অথবা করুণা অথবা নিরপেক্ষ]
MANIPULATION: [কীভাবে আবেগ ব্যবহার করা হচ্ছে ১ লাইনে]
CATEGORY: [রাজনীতি অথবা স্বাস্থ্য অথবা ধর্ম অথবা বিনোদন অথবা আন্তর্জাতিক অথবা দুর্ঘটনা অথবা অন্যান্য]
RED FLAGS:
- [সমস্যা ১]
- [সমস্যা ২]
- [সমস্যা ৩]
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content

    verdict = reason = emotion = manipulation = category = ""
    confidence_num = 50
    red_flags = []

    for line in result.strip().split('\n'):
        if line.startswith("VERDICT:"):
            verdict = line.replace("VERDICT:", "").strip()
        elif line.startswith("CONFIDENCE:"):
            try:
                confidence_num = int(line.replace("CONFIDENCE:", "").strip().replace("%", ""))
            except:
                confidence_num = 50
        elif line.startswith("কারণ:"):
            reason = line.replace("কারণ:", "").strip()
        elif line.startswith("EMOTION:"):
            emotion = line.replace("EMOTION:", "").strip()
        elif line.startswith("MANIPULATION:"):
            manipulation = line.replace("MANIPULATION:", "").strip()
        elif line.startswith("CATEGORY:"):
            category = line.replace("CATEGORY:", "").strip()
        elif line.startswith("- "):
            red_flags.append(line.replace("- ", "").strip())

    return {
        "verdict": verdict,
        "confidence": confidence_num,
        "reason": reason,
        "emotion": emotion,
        "manipulation": manipulation,
        "category": category,
        "red_flags": red_flags
    }
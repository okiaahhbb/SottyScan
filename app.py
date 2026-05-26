import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🔍 সত্যScan")
st.markdown("বাংলা নিউজ paste করুন, আমরা বলব এটা কতটা সত্যি।")

text = st.text_area("নিউজটি এখানে লিখুন:", height=200)

if st.button("যাচাই করুন ✅"):
    if text:
        with st.spinner("বিশ্লেষণ করা হচ্ছে..."):
            prompt = f"""
            তুমি একজন বাংলাদেশের expert fact-checker।
            নিচের বাংলা নিউজটি বিশ্লেষণ করো।

            নিউজ: {text}

            এই format এ বাংলায় উত্তর দাও:
            VERDICT: [সত্যি / মিথ্যা / সন্দেহজনক]
            CONFIDENCE: [০-১০০]%
            কারণ: [২-৩ লাইনে বলো কেন]
            EMOTION: [ভয় / রাগ / ধর্মীয় উস্কানি / দেশপ্রেম / করুণা / নিরপেক্ষ]
            RED FLAGS: [সমস্যাগুলো আলাদা লাইনে]
            """
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.markdown("### 📊 বিশ্লেষণ:")
            st.write(result)
    else:
        st.warning("আগে কিছু লিখুন!")
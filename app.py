import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(
    page_title="সত্যScan",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&display=swap');
* { font-family: 'Hind Siliguri', sans-serif; }
[data-testid="stAppViewContainer"] {
    background-image: url("app/static/bg.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(5, 5, 20, 0.82);
    z-index: 0;
}
[data-testid="stSidebar"] {
    background: rgba(5, 5, 20, 0.92) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] * { color: #c8d6e5 !important; }
section.main > div { position: relative; z-index: 1; }
.hero { text-align: center; padding: 3rem 1rem 2rem; }
.breaking {
    background: #e84560;
    color: white;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 4px 16px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 1rem;
}
.hero h1 {
    font-size: 4rem;
    font-weight: 700;
    color: white;
    margin: 0;
    text-shadow: 0 2px 20px rgba(0,0,0,0.5);
}
.hero h1 span { color: #e84560; }
.hero p { color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 0.5rem; }
.verdict-fake {
    background: rgba(232,69,96,0.15);
    border: 2px solid #e84560;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #ff6b8a;
    margin: 1rem 0;
}
.verdict-real {
    background: rgba(0,184,148,0.15);
    border: 2px solid #00b894;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #55efc4;
    margin: 1rem 0;
}
.verdict-suspicious {
    background: rgba(253,203,110,0.15);
    border: 2px solid #fdcb6e;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #ffeaa7;
    margin: 1rem 0;
}
.stat-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}
.stat-box .num { font-size: 2.2rem; font-weight: 700; color: #e84560; }
.stat-box .lbl { color: rgba(255,255,255,0.5); font-size: 0.8rem; margin-top: 4px; }
.flag-item {
    background: rgba(232,69,96,0.1);
    border-left: 3px solid #e84560;
    padding: 0.7rem 1rem;
    border-radius: 0 8px 8px 0;
    margin: 0.4rem 0;
    color: #ffb3c1;
    font-size: 0.95rem;
}
.reason-box {
    background: rgba(255,255,255,0.05);
    border-left: 3px solid #74b9ff;
    padding: 1rem 1.2rem;
    border-radius: 0 8px 8px 0;
    color: rgba(255,255,255,0.85);
    font-size: 0.95rem;
    line-height: 1.7;
}
.manipulation-box {
    background: rgba(253,203,110,0.08);
    border-left: 3px solid #fdcb6e;
    padding: 1rem 1.2rem;
    border-radius: 0 8px 8px 0;
    color: #ffeaa7;
    font-size: 0.95rem;
    line-height: 1.7;
    margin-top: 1rem;
}
.section-head {
    color: white;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    opacity: 0.9;
}
.history-item {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 0.6rem 0.8rem;
    margin: 0.3rem 0;
    font-size: 0.8rem;
    color: #c8d6e5;
}
textarea {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="breaking">🔴 LIVE FACT CHECK</div>
    <h1>সত্য<span>Scan</span></h1>
    <p>বাংলাদেশের প্রথম AI-powered Emotional Manipulation Detector</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🔍 সত্যScan")
    st.markdown("---")
    st.markdown("**📌 কীভাবে ব্যবহার করবেন**")
    st.markdown("১. নিউজ paste করুন")
    st.markdown("২. যাচাই করুন চাপুন")
    st.markdown("৩. AI রিপোর্ট দেখুন")
    st.markdown("---")
    st.markdown("**🚩 Fake News এর লক্ষণ**")
    st.markdown("• উৎস উল্লেখ নেই")
    st.markdown("• অতিরিক্ত আবেগময় ভাষা")
    st.markdown("• Sensational headline")
    st.markdown("• অস্পষ্ট তারিখ")
    st.markdown("---")
    st.markdown("**✅ নির্ভরযোগ্য সূত্র**")
    st.markdown("[Prothom Alo](https://prothomalo.com)")
    st.markdown("[BBC Bangla](https://bbc.com/bengali)")
    st.markdown("[Daily Star](https://thedailystar.net)")

    if st.session_state.history:
        st.markdown("---")
        st.markdown("**📋 আগের যাচাই**")
        for item in reversed(st.session_state.history[-5:]):
            if "মিথ্যা" in item["verdict"]:
                icon = "🔴"
            elif "সত্যি" in item["verdict"]:
                icon = "🟢"
            else:
                icon = "🟡"
            st.markdown(f'<div class="history-item">{icon} {item["text"]}</div>', unsafe_allow_html=True)

text = st.text_area(
    "📰 নিউজটি এখানে paste করুন:",
    height=160,
    placeholder="এখানে বাংলা নিউজ লিখুন বা paste করুন..."
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("🔍 এখনই যাচাই করুন", use_container_width=True, type="primary")

if analyze:
    if text:
        with st.spinner("🤖 AI বিশ্লেষণ করছে..."):
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

            verdict = reason = emotion = manipulation = ""
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
                elif line.startswith("- "):
                    red_flags.append(line.replace("- ", "").strip())

            st.session_state.history.append({
                "text": text[:60] + "...",
                "verdict": verdict,
                "confidence": confidence_num,
                "emotion": emotion
            })

            if "মিথ্যা" in verdict:
                st.markdown(f'<div class="verdict-fake">❌ {verdict}</div>', unsafe_allow_html=True)
            elif "সত্যি" in verdict:
                st.markdown(f'<div class="verdict-real">✅ {verdict}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="verdict-suspicious">⚠️ {verdict}</div>', unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f'<div class="stat-box"><div class="num">{confidence_num}%</div><div class="lbl">Confidence</div></div>', unsafe_allow_html=True)
            with c2:
                emotion_icons = {"ভয়": "😱", "রাগ": "😡", "ধর্মীয়": "🕌", "দেশপ্রেম": "🇧🇩", "করুণা": "😢", "নিরপেক্ষ": "😐"}
                icon = "🧠"
                for key, val in emotion_icons.items():
                    if key in emotion:
                        icon = val
                        break
                st.markdown(f'<div class="stat-box"><div class="num">{icon}</div><div class="lbl">{emotion}</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="stat-box"><div class="num">{len(red_flags)}</div><div class="lbl">Red Flags</div></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            col_l, col_r = st.columns(2)
            with col_l:
                st.markdown('<div class="section-head">💡 কারণ</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="reason-box">{reason if reason else "বিশ্লেষণ দেখুন"}</div>', unsafe_allow_html=True)
                if manipulation:
                    st.markdown('<div class="section-head" style="margin-top:1rem;">🧠 Manipulation Tactic</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="manipulation-box">{manipulation}</div>', unsafe_allow_html=True)

            with col_r:
                st.markdown('<div class="section-head">🚩 Red Flags</div>', unsafe_allow_html=True)
                if red_flags:
                    for flag in red_flags:
                        st.markdown(f'<div class="flag-item">❌ {flag}</div>', unsafe_allow_html=True)
                else:
                    st.success("কোনো red flag নেই ✅")

            st.markdown("<br>", unsafe_allow_html=True)
            st.progress(confidence_num / 100)
            st.caption(f"AI Confidence Score: {confidence_num}%")
    else:
        st.warning("⚠️ আগে কিছু লিখুন!")
    
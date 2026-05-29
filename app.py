import streamlit as st
from analyzer import analyze_news
from utils import extract_text_from_url
from ui import load_css, show_hero, show_sidebar, show_result

if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(
    page_title="সত্যScan",
    page_icon="🔍",
    layout="wide"
)

load_css()
show_hero()
show_sidebar(st.session_state.history)

tab1, tab2, tab3 = st.tabs(["📝 Text Paste", "🔗 URL দিন", "📸 Image/Screenshot"])

text = ""
with tab1:
    text = st.text_area(
        "📰 নিউজটি এখানে paste করুন:",
        height=160,
        placeholder="এখানে বাংলা নিউজ লিখুন বা paste করুন..."
    )

with tab2:
    url = st.text_input("🔗 নিউজের link দিন:", placeholder="https://prothomalo.com/...")
    if url:
        extracted = extract_text_from_url(url)
        if extracted:
            text = extracted
            st.success(f"✅ {len(extracted)} characters extract হয়েছে!")
        else:
            st.error("❌ URL থেকে text extract করা যায়নি।")

with tab3:
    uploaded = st.file_uploader("Screenshot বা Image upload করুন:", type=["png", "jpg", "jpeg"])
    if uploaded:
        from utils import extract_text_from_image
        extracted = extract_text_from_image(uploaded)
        if extracted:
            text = extracted
            st.success(f"✅ {len(extracted)} characters extract হয়েছে!")
            st.text_area("Extract হওয়া text:", value=extracted, height=100)
        else:
            st.error("❌ Image থেকে text extract করা যায়নি।")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("🔍 এখনই যাচাই করুন", use_container_width=True, type="primary")

if analyze:
    if text:
        with st.spinner("🤖 AI বিশ্লেষণ করছে..."):
            result = analyze_news(text)

            st.session_state.history.append({
                "text": text[:60] + "...",
                "verdict": result["verdict"],
                "confidence": result["confidence"],
                "emotion": result["emotion"]
            })

            show_result(result)
    else:
        st.warning("⚠️ আগে কিছু লিখুন বা URL দিন!")
import streamlit as st

def load_css():
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
.hero h1 { font-size: 4rem; font-weight: 700; color: white; margin: 0; text-shadow: 0 2px 20px rgba(0,0,0,0.5); }
.hero h1 span { color: #e84560; }
.hero p { color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 0.5rem; }
.verdict-fake { background: rgba(232,69,96,0.15); border: 2px solid #e84560; border-radius: 12px; padding: 1.5rem; text-align: center; font-size: 2rem; font-weight: 700; color: #ff6b8a; margin: 1rem 0; }
.verdict-real { background: rgba(0,184,148,0.15); border: 2px solid #00b894; border-radius: 12px; padding: 1.5rem; text-align: center; font-size: 2rem; font-weight: 700; color: #55efc4; margin: 1rem 0; }
.verdict-suspicious { background: rgba(253,203,110,0.15); border: 2px solid #fdcb6e; border-radius: 12px; padding: 1.5rem; text-align: center; font-size: 2rem; font-weight: 700; color: #ffeaa7; margin: 1rem 0; }
.stat-box { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1.2rem; text-align: center; }
.stat-box .num { font-size: 2.2rem; font-weight: 700; color: #e84560; }
.stat-box .lbl { color: rgba(255,255,255,0.5); font-size: 0.8rem; margin-top: 4px; }
.flag-item { background: rgba(232,69,96,0.1); border-left: 3px solid #e84560; padding: 0.7rem 1rem; border-radius: 0 8px 8px 0; margin: 0.4rem 0; color: #ffb3c1; font-size: 0.95rem; }
.reason-box { background: rgba(255,255,255,0.05); border-left: 3px solid #74b9ff; padding: 1rem 1.2rem; border-radius: 0 8px 8px 0; color: rgba(255,255,255,0.85); font-size: 0.95rem; line-height: 1.7; }
.manipulation-box { background: rgba(253,203,110,0.08); border-left: 3px solid #fdcb6e; padding: 1rem 1.2rem; border-radius: 0 8px 8px 0; color: #ffeaa7; font-size: 0.95rem; line-height: 1.7; margin-top: 1rem; }
.category-badge { display: inline-block; padding: 4px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; margin: 0.5rem 0; }
.section-head { color: white; font-size: 1rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.8rem; opacity: 0.9; }
.history-item { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 0.8rem; margin: 0.3rem 0; font-size: 0.8rem; color: #c8d6e5; }
.highlight-box { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1.2rem; line-height: 2; font-size: 0.95rem; color: rgba(255,255,255,0.85); }
.suspicious-word { background: rgba(232,69,96,0.3); color: #ff6b8a; padding: 2px 6px; border-radius: 4px; font-weight: 700; border: 1px solid rgba(232,69,96,0.5); }
.word-badge { display: inline-block; background: rgba(232,69,96,0.15); border: 1px solid #e84560; color: #ff6b8a; padding: 3px 10px; border-radius: 12px; font-size: 0.8rem; margin: 3px; }
textarea { background: rgba(255,255,255,0.07) !important; border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 12px !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

def show_hero():
    st.markdown("""
<div class="hero">
    <div class="breaking">🔴 LIVE FACT CHECK</div>
    <h1>সত্য<span>Scan</span></h1>
    <p>বাংলাদেশের প্রথম AI-powered Emotional Manipulation Detector</p>
</div>
""", unsafe_allow_html=True)

def show_sidebar(history):
    with st.sidebar:
        st.markdown("## 🔍 সত্যScan")
        st.markdown("---")
        st.markdown("**📌 কীভাবে ব্যবহার করবেন**")
        st.markdown("১. নিউজ paste করুন বা URL দিন")
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
        if history:
            st.markdown("---")
            st.markdown("**📋 আগের যাচাই**")
            for item in reversed(history[-5:]):
                if "মিথ্যা" in item["verdict"]:
                    icon = "🔴"
                elif "সত্যি" in item["verdict"]:
                    icon = "🟢"
                else:
                    icon = "🟡"
                st.markdown(f'<div class="history-item">{icon} {item["text"]}</div>', unsafe_allow_html=True)

def highlight_text(text, suspicious_words):
    if not suspicious_words:
        return text
    words = [w.strip() for w in suspicious_words.split(',') if w.strip()]
    highlighted = text
    for word in words:
        if word and word in highlighted:
            highlighted = highlighted.replace(
                word,
                f'<span class="suspicious-word">⚠️ {word}</span>'
            )
    return highlighted

def show_result(data, original_text=""):
    verdict = data["verdict"]
    confidence = data["confidence"]
    emotion = data["emotion"]
    reason = data["reason"]
    manipulation = data["manipulation"]
    category = data["category"]
    red_flags = data["red_flags"]
    suspicious_words = data.get("suspicious_words", "")

    if "মিথ্যা" in verdict:
        st.markdown(f'<div class="verdict-fake">❌ {verdict}</div>', unsafe_allow_html=True)
    elif "সত্যি" in verdict:
        st.markdown(f'<div class="verdict-real">✅ {verdict}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="verdict-suspicious">⚠️ {verdict}</div>', unsafe_allow_html=True)

    category_colors = {
        "রাজনীতি": "background:#1a1a5e;color:#7986cb;",
        "স্বাস্থ্য": "background:#1b5e20;color:#66bb6a;",
        "ধর্ম": "background:#4a148c;color:#ce93d8;",
        "বিনোদন": "background:#880e4f;color:#f48fb1;",
        "আন্তর্জাতিক": "background:#006064;color:#80deea;",
        "দুর্ঘটনা": "background:#b71c1c;color:#ef9a9a;",
        "অন্যান্য": "background:#212121;color:#bdbdbd;"
    }
    cat_style = category_colors.get(category, "background:#212121;color:#bdbdbd;")
    if category:
        st.markdown(f'<span class="category-badge" style="{cat_style}">📂 {category}</span>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="num">{confidence}%</div><div class="lbl">Confidence</div></div>', unsafe_allow_html=True)
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

    if suspicious_words and original_text:
        st.markdown('<div class="section-head">🔦 Suspicious Words Highlighted</div>', unsafe_allow_html=True)
        words_list = [w.strip() for w in suspicious_words.split(',') if w.strip()]
        if words_list:
            badges = " ".join([f'<span class="word-badge">⚠️ {w}</span>' for w in words_list])
            st.markdown(f'<div style="margin-bottom:0.8rem;">{badges}</div>', unsafe_allow_html=True)
        highlighted = highlight_text(original_text[:500], suspicious_words)
        st.markdown(f'<div class="highlight-box">{highlighted}...</div>', unsafe_allow_html=True)
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
    st.progress(confidence / 100)
    st.caption(f"AI Confidence Score: {confidence}%")
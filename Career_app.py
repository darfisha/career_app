import streamlit as st
import pandas as pd
import time

# Page config
st.set_page_config(page_title="Find Your Future 🇮🇳✨", layout="centered")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_excel("career_data.xlsx")

df = load_data()

# Title and header
st.markdown("""
<style>
.big-font {
    font-size:45px !important;
    text-align: center;
    color: #6a1b9a;
}
.subtitle {
    font-size:20px;
    text-align: center;
    color: #444;
}
.centered {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p class='big-font'>🔮 Find Your Future | AI-Powered Career Guide for Indian Students 🇮🇳</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Let AI help you find where you truly belong... 🎓📊💻🚀</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 1. Input Section ---
st.markdown("## 🧭 Let’s Get Started")

stream = st.selectbox("🔍 What’s your academic stream?", ["Science 🔬", "Commerce 💰", "Arts 🎨"])
aspiration = st.text_input("🌟 What’s your dream career or aspiration? (e.g., IAS Officer, Lawyer, Data Scientist)")
show = st.button("🚀 Show Me My Career Path!")

# --- 2. Output Section ---
if show:
    # Extract the actual stream
    selected_stream = stream.split(" ")[0].lower()

    # Filter logic (match stream and check if aspiration keyword is in any field)
    df['Stream'] = df['Stream'].str.lower()
    df_match = df[df['Stream'] == selected_stream]

    if aspiration:
        df_match = df_match[df_match.apply(lambda row: aspiration.lower() in str(row['Career']).lower() or aspiration.lower() in str(row['Typical Job Titles']).lower(), axis=1)]

    # If match found
    if not df_match.empty:
        result = df_match.sample(1).iloc[0]

        # Output with animations
        st.markdown("## 🎯 Your AI-Powered Career Match")
        with st.container():
            time.sleep(1)
            st.markdown(f"### 💼 Career: **{result['Career']}**")

            time.sleep(1)
            st.markdown(f"**📝 Exams to Prepare For:** {result['Exams']}")
            time.sleep(1)
            st.markdown(f"**🛠️ Required Skills:** {result['Required Skills']}")
            time.sleep(1)
            st.markdown(f"**🎓 Education Needed:** {result['Education Level Required']}")
            time.sleep(1)
            st.markdown(f"**💸 Salary Range (India):** {result['Salary Range (INR/year)']}")
            time.sleep(1)
            st.markdown(f"**🌐 Work Environment:** {result['Work Environment']}")
            time.sleep(1)
            st.markdown(f"**🏢 Related Industries:** {result['Related Industries']}")
            time.sleep(1)
            st.markdown(f"**🧑‍💼 Typical Job Titles:** {result['Typical Job Titles']}")
            time.sleep(1)
            st.markdown(f"**🧠 Personality Traits:** {result['Personality Traits']}")
            time.sleep(1)
            st.markdown(f"**📜 Certifications:** {result['Certifications']}")
            time.sleep(1)
            st.markdown(f"**⏰ Typical Work Hours:** {result['Typical Work Hours']}")
    else:
        st.warning("🤷‍♀️ No exact match found. Try changing your aspiration or stream!")

    st.markdown("---")
    if st.button("🔁 Try Again"):
        st.experimental_rerun()

# --- Footer ---
st.markdown("""
<hr style="margin-top: 30px; margin-bottom: 10px;">
<div style='text-align: center; color: gray;'>
    Made with ❤️ by <b>Darfisha Shaikh</b> for <i>Hack the Haze 2025</i> 💻🎉
</div>
""", unsafe_allow_html=True)

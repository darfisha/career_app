import streamlit as st
import pandas as pd
import time
import base64
from streamlit_lottie import st_lottie
import json

# --- Page Config ---
st.set_page_config(page_title="AI Career Guide 🇮🇳", layout="centered")

# --- Background Image ---
def add_bg_local():
    with open("background.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_local()





# --- Load Dataset ---
@st.cache_data
def load_data():
    df = pd.read_excel("career_data.xlsx")
    df['Required Skills'] = df['Required Skills'].apply(lambda x: [skill.strip() for skill in x.split(',')])
    return df
df = load_data()

# --- Animated Header ---
st.markdown("<h1 style='text-align:center;'>🚀 AI Career Guide for Indian Students 🇮🇳</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Let’s find your perfect path... 🎯</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Input Section ---
stream_options = {"Science 🔬": "Science", "Commerce 💰": "Commerce", "Arts 🎨": "Arts"}
stream_choice = st.selectbox("Your Academic Stream", list(stream_options.keys()))
selected_stream = stream_options[stream_choice]
career_aspiration = st.text_input("Your dream job (e.g., Lawyer, IAS Officer, Data Analyst)")
submit = st.button("🔍 Reveal My Career Path")

# --- Animation Functions ---
def typing_effect(text, speed=0.01):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"### {typed}")
        time.sleep(speed)

def reveal_section(title, content, delay=0.5):
    typing_effect(title)
    st.markdown(content)
    time.sleep(delay)

# --- Main Logic ---
if submit:
    with st.spinner("🔄 Analyzing your stream and aspiration..."):
        time.sleep(2)
    st.progress(100)

    filtered_df = df[df['Stream'].str.lower() == selected_stream.lower()]
    if career_aspiration.strip():
        filtered_df = filtered_df[filtered_df['Career'].str.contains(career_aspiration.strip(), case=False, na=False)]

    if filtered_df.empty:
        st.warning("😔 No match found. Try refining your input.")
    else:
        career_info = filtered_df.iloc[0]
        

        for emoji in "✨✨✨✨✨✨":
            st.markdown(f"<h2 style='text-align:center;'>{emoji}</h2>", unsafe_allow_html=True)
            time.sleep(0.1)

        reveal_section("🎯 Career Name", f"**{career_info['Career']}**")
        reveal_section("📚 Exams to Prepare For", career_info['Exams'])
        reveal_section("🛠️ Required Skills", ", ".join(career_info['Required Skills']))
        reveal_section("🎓 Education Needed", career_info['Education Level Required'])
        reveal_section("💸 Salary Range (INR/year)", career_info['Salary Range (INR/year)'])
        reveal_section("🌐 Work Environment", career_info['Work Environment'])
        reveal_section("🏢 Related Industries", career_info['Related Industries'])
        reveal_section("🧑‍💼 Typical Job Titles", career_info['Typical Job Titles'])
        reveal_section("🧠 Personality Traits", career_info['Personality Traits'])

        st.markdown("---")
        st.markdown("""
        <h3 style="text-align:center; animation: blink 1s infinite;">
            🌟 Believe in yourself — your dream career awaits! 🌟
        </h3>
        <style>
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.2; }
            100% { opacity: 1; }
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("🔁 Start Over"):
            st.experimental_rerun()
else:
    st.info("Choose a stream and type in your dream job to start.")

# --- Footer ---
st.markdown("""
<hr>
<div style='text-align:center; font-size:14px; color:#555;'>
    Made with ❤️ by <strong>Darfisha Shaikh</strong> for Hack the Haze 2025 🎉
</div>
""", unsafe_allow_html=True)

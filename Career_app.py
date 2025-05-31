import streamlit as st
import pandas as pd
import time
import base64
from streamlit_extras.let_it_rain import rain

# --- Page Config ---
st.set_page_config(
    page_title="Find Your Future: India’s AI Career Guide 🇮🇳✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Background Image (local file) ---
def add_bg_local():
    with open("background.jpg", "rb") as image_file:
        encoded_string = image_file.read()
    b64 = base64.b64encode(encoded_string).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpg;base64,{b64}");
             background-attachment: fixed;
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
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
    # Process skills into list
    df['Required Skills'] = df['Required Skills'].apply(lambda x: [skill.strip() for skill in x.split(',')])
    return df

df = load_data()

# --- Header ---
st.markdown("""
    <h1 style='text-align:center; color:#ff5722; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;'>
        Find Your Future 🔮 | AI-Powered Career Guide for Indian Students 🇮🇳
    </h1>
    <p style='text-align:center; font-size:18px; color:#6a1b9a;'>
        Let AI help you find where you truly belong... 🎓📊💻🚀
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- User Input Section ---
stream_options = {
    "Science 🔬": "Science",
    "Commerce 💰": "Commerce",
    "Arts 🎨": "Arts"
}

st.markdown("### What's your academic stream?")
stream_choice = st.selectbox("", options=list(stream_options.keys()))
selected_stream = stream_options[stream_choice]

career_aspiration = st.text_input("What's your dream career or aspiration? (e.g., IAS Officer, Lawyer, Data Scientist)")

submit = st.button("🚀 Show Me My Career Path!")

st.markdown("---")

if submit:
    # Filter by stream
    filtered_df = df[df['Stream'].str.lower() == selected_stream.lower()]
    # Filter by career aspiration keyword (case insensitive contains)
    if career_aspiration.strip() != "":
        filtered_df = filtered_df[filtered_df['Career'].str.contains(career_aspiration.strip(), case=False, na=False)]

    if filtered_df.empty:
        st.warning("😞 Oops! No matching careers found. Try different stream or aspiration keywords.")
    else:
        st.success("🎉 Yay! We found some career paths matching your interests! ✨")

        # For simplicity show first match only
        career_info = filtered_df.iloc[0]

        # Helper to show each section with emoji rain animation
        def reveal_section(title, content, emoji="✨", delay=1.5):
            rain(emoji, speed=10, drop_length=7, drop_radius=5, fall_angle=90)
            st.markdown(f"### {title}")
            st.markdown(f"{content}")
            time.sleep(delay)

        reveal_section("🎯 Career Name", f"**{career_info['Career']}**", emoji="🎯")
        reveal_section("📚 Exams to Prepare For", career_info['Exams'], emoji="📚")
        reveal_section("🛠️ Required Skills", ", ".join(career_info['Required Skills']), emoji="🛠️")
        reveal_section("🎓 Education Needed", career_info['Education Level Required'], emoji="🎓")
        reveal_section("💸 Salary Range (INR/year)", career_info['Salary Range (INR/year)'], emoji="💸")
        reveal_section("🌐 Work Environment", career_info['Work Environment'], emoji="🌐")
        reveal_section("🏢 Related Industries", career_info['Related Industries'], emoji="🏢")
        reveal_section("🧑‍💼 Typical Job Titles", career_info['Typical Job Titles'], emoji="🧑‍💼")
        reveal_section("🧠 Personality Traits That Fit This Role", career_info['Personality Traits'], emoji="🧠")

        st.markdown("---")

        st.markdown("""
        <div style='background-color:#fff3e0; padding:15px; border-radius:8px; color:#bf360c; font-weight:bold;'>
            ✨ Remember, every great journey begins with a single step. Keep learning and stay curious — your future is bright! 🚀🇮🇳
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔁 Try Again"):
            st.experimental_rerun()
else:
    st.info("Fill out your stream and career aspiration above, then click the button to find your path! ✨")

# --- Footer ---
st.markdown("""
<hr style="margin-top:40px; margin-bottom:20px;">
<div style='text-align:center; color:#555; font-size:14px;'>
    Made with ❤️ by <strong>Darfisha Shaikh</strong> for Hack the Haze 2025 💻🎉
</div>
""", unsafe_allow_html=True)

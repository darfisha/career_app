import streamlit as st
import pandas as pd
import base64
import time
from streamlit_extras.let_it_rain import rain

# Page config
st.set_page_config(page_title="Find Your Future", layout="wide")

# Set background image
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("background.jpg")  # Ensure the image is in the same directory

# Title and Subtitle
st.markdown("""
    <h1 style='text-align: center;'>Find Your Future 🔮 | AI-Powered Career Guide for Indian Students 🇮🇳</h1>
    <h4 style='text-align: center;'>Let AI help you find where you truly belong... 🎓📊💻🚀</h4>
""", unsafe_allow_html=True)

# Welcome animation
rain(emoji="🎉", font_size=40, falling_speed=5, animation_length="medium")

# Load Data
df = pd.read_excel("career_data.xlsx") 

# Rename columns for easier reference
df.columns = ["Career", "Stream", "Required Skills", "Exams", "Education", "Salary", "Job Demand",
              "Work Environment", "Soft Skills", "Duration", "Related Industries", "Typical Job Titles",
              "Personality Traits", "Certifications", "Typical Work Hours"]

# Drop unwanted columns
df = df.drop(columns=["Certifications", "Typical Work Hours"])

# Input section
st.markdown("## 🎯 Choose Your Preferences")

col1, col2 = st.columns(2)

with col1:
    stream = st.selectbox("What’s your academic stream?", ["Science 🔬", "Commerce 💰", "Arts 🎨"])

with col2:
    aspiration = st.text_input("What’s your dream career or aspiration? (e.g., IAS Officer, Lawyer, Data Scientist)")

if st.button("🚀 Show Me My Career Path!"):
    # Celebratory animation
    rain(emoji="✨", font_size=30, falling_speed=4, animation_length="long")

    # Filter data
    filtered_df = df[df['Stream'].str.lower().str.contains(stream.split()[0].lower())]
    if aspiration:
        filtered_df = filtered_df[filtered_df['Career'].str.lower().str.contains(aspiration.lower())]

    if not filtered_df.empty:
        career_info = filtered_df.iloc[0]

        st.markdown(f"### 👩‍💼 **Your Ideal Career Match: {career_info['Career']}**")

        time.sleep(0.5)
        st.markdown(f"**📝 Exams to Prepare For:** {career_info['Exams']}")

        time.sleep(0.5)
        st.markdown(f"**🛠️ Required Skills:** {career_info['Required Skills']}")

        time.sleep(0.5)
        st.markdown(f"**🎓 Education Needed:** {career_info['Education']}")

        time.sleep(0.5)
        st.markdown(f"**💸 Salary Range in India:** {career_info['Salary']}")

        time.sleep(0.5)
        st.markdown(f"**🌐 Work Environment:** {career_info['Work Environment']}")

        time.sleep(0.5)
        st.markdown(f"**🏢 Industries You’ll Work In:** {career_info['Related Industries']}")

        time.sleep(0.5)
        st.markdown(f"**🧑‍💼 Typical Job Titles:** {career_info['Typical Job Titles']}")

        time.sleep(0.5)
        st.markdown(f"**🧠 Personality Traits That Fit This Role:** {career_info['Personality Traits']}")

        time.sleep(0.5)
        st.markdown(f"**📊 Duration of Study:** {career_info['Duration']}")

        st.success("🌟 Keep learning, keep growing. The future belongs to you!")
    else:
        st.warning("😕 Sorry, no exact match found. Try a different stream or aspiration.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
    Made with ❤️ by Darfisha Shaikh for Hack the Haze 2025 💻🎉<br>
    <button onclick="window.location.reload();">🔁 Try Again</button>
    </div>
""", unsafe_allow_html=True)


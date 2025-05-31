import streamlit as st
import pandas as pd
import base64
from io import BytesIO
import random

# Load the dataset with error handling and caching
@st.cache_data

def load_data():
    try:
        df = pd.read_excel("career_data.xlsx")
        df['Required Skills'] = df['Required Skills'].apply(lambda x: [skill.strip().lower() for skill in x.split(',')])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=['Career', 'Required Skills', 'Stream', 'Exams'])

# Load data
df = load_data()

# Fun background colors
page_bg_img = '''
<style>
body {
background-image: linear-gradient(to bottom right, #f7e7ff, #e0f7fa);
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='text-align: center; color: #6a1b9a;'>✨ Career Genie 🧞‍♂️</h1>
<p style='text-align: center;'>Find magical career paths based on your talents and interests! 🧭</p>
""", unsafe_allow_html=True)

# --- Stream Selection ---
stream_map = {
    "🔬 Science": "Science",
    "💼 Commerce": "Commerce",
    "🎨 Arts/Humanities": "Arts",
    "❓ Not Sure": "Not Sure"
}

st.markdown("### 🎓 Choose Your Stream")
stream_choice = st.radio("Which academic world do you belong to?", list(stream_map.keys()), horizontal=True)
selected_stream = stream_map[stream_choice]

# --- Skill Selection ---
all_skills = sorted({skill.strip().lower() for skills in df['Required Skills'] for skill in skills})
emoji_skills = {
    "programming": "💻", "leadership": "🧑‍💼", "communication": "🗣️",
    "creativity": "🎨", "data analysis": "📊", "problem solving": "🧠",
    "teaching": "📚", "empathy": "❤️", "law": "

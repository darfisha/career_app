import streamlit as st
import pandas as pd
import base64
from io import BytesIO
import random

# Load the dataset
df = pd.read_excel("career_data.xlsx")
df['Required_skills'] = df['Required_skills'].apply(lambda x: [skill.strip().lower() for skill in x.split(',')])

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
all_skills = sorted({skill.strip().lower() for skills in df['required_skills'] for skill in skills})
emoji_skills = {
    "programming": "💻", "leadership": "🧑‍💼", "communication": "🗣️",
    "creativity": "🎨", "data analysis": "📊", "problem solving": "🧠",
    "teaching": "📚", "empathy": "❤️", "law": "⚖️", "biology": "🧬",
    "teamwork": "🤝", "research": "🔍"
}

skill_display = [f"{emoji_skills.get(skill, '⭐')} {skill.title()}" for skill in all_skills]
skill_map = dict(zip(skill_display, all_skills))

st.markdown("### 🛠️ Select Your Magical Skills")
selected_skills_display = st.multiselect("Pick the skills that describe your strengths:", options=skill_display)
selected_skills = [skill_map[s] for s in selected_skills_display]

# --- Filter Logic ---
def match_skills(row):
    return all(skill in row['required_skills'] for skill in selected_skills)

if selected_stream != "Not Sure":
    filtered_df = df[df['stream'].str.lower() == selected_stream.lower()]
else:
    filtered_df = df.copy()

if selected_skills:
    filtered_df = filtered_df[filtered_df.apply(match_skills, axis=1)]

# --- Display Career Suggestions ---
if not filtered_df.empty:
    st.markdown("## 🔍 Your Dream Careers")
    st.success(random.choice([
        "Great picks! Here’s what suits you best! 🌟",
        "These careers match your vibe perfectly! 💼",
        "Based on your skills, these roles await you! 🚀"
    ]))

    filtered_df_display = filtered_df.copy()
    filtered_df_display['required_skills'] = filtered_df_display['required_skills'].apply(lambda x: ", ".join([skill.title() for skill in x]))
    filtered_df_display.columns = ['Career 👩‍💼', 'Required Skills 🛠️', 'Stream 🎓', 'Exams 📝']
    st.dataframe(filtered_df_display, use_container_width=True)

    # Download CSV
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df_display)
    st.download_button("📥 Download Career Report as CSV", csv, "career_suggestions.csv", "text/csv")
else:
    st.warning("Oops! No matching careers found. Try tweaking your stream or skill selections! 🤔")

# --- Reset Button ---
if st.button("🔄 Start Over"):
    st.experimental_rerun()

# --- Footer ---
st.markdown("""
---
<div style='text-align: center;'>
    Made with ❤️ by <strong>Darfisha Shaikh</strong> for <em>Hack the Haze</em> 🌈
</div>
""", unsafe_allow_html=True)

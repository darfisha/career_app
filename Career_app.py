import streamlit as st
import pandas as pd
import base64
from io import BytesIO
import random
import time

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

# Fun background colors and animation styles
page_bg_img = '''
<style>
body {
background-image: linear-gradient(to bottom right, #f7e7ff, #e0f7fa);
background-size: cover;
font-family: 'Segoe UI', sans-serif;
}
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
.bounce {
  animation: bounce 2s infinite;
  display: inline-block;
}
.fadeIn {
  animation: fadeIn 1s ease-in;
}
.dataframe-style {
  border: 2px solid #6a1b9a;
  border-radius: 10px;
  padding: 10px;
  background-color: #ffffffcc;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title with animation
st.markdown("""
<h1 style='text-align: center; color: #6a1b9a;' class='bounce'>✨ Career Genie 🧞‍♂️</h1>
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
    "teaching": "📚", "empathy": "❤️", "law": "⚖️", "biology": "🧬",
    "teamwork": "🤝", "research": "🔍"
}

skill_display = [f"{emoji_skills.get(skill, '⭐')} {skill.title()}" for skill in all_skills]
skill_map = dict(zip(skill_display, all_skills))

st.markdown("### 🛠️ Select Your Magical Skills")
selected_skills_display = st.multiselect("Pick the skills that describe your strengths:", options=skill_display)
selected_skills = [skill_map[s] for s in selected_skills_display]

# --- Filter Logic ---
if selected_stream != "Not Sure":
    filtered_df = df[df['Stream'].str.lower() == selected_stream.lower()]
else:
    filtered_df = df.copy()

if selected_skills:
    filtered_df = filtered_df[filtered_df['Required Skills'].apply(lambda x: set(selected_skills).issubset(set(x)))]

# --- Display Career Suggestions ---
if not filtered_df.empty:
    st.markdown("## 🔍 Your Dream Careers")
    st.success(random.choice([
        "Great picks! Here’s what suits you best! 🌟",
        "These careers match your vibe perfectly! 💼",
        "Based on your skills, these roles await you! 🚀"
    ]))

    time.sleep(1)  # Subtle delay before showing results

    filtered_df_display = filtered_df.copy()
    filtered_df_display['Required Skills'] = filtered_df_display['Required Skills'].apply(lambda x: ", ".join([skill.title() for skill in x]))

    # Extended columns to show more career info
    columns_to_display = [
        'Career', 'Required Skills', 'Stream', 'Exams', 'Education Level Required',
        'Salary Range (INR/year)', 'Job Demand', 'Work Environment', 'Soft Skills',
        'Duration of Study', 'Related Industries', 'Typical Job Titles',
        'Personality Traits', 'Certifications', 'Typical Work Hours'
    ]
    columns_renamed = [
        'Career 👩‍💼', 'Required Skills 🛠️', 'Stream 🎓', 'Exams 📝', 'Education 🎓',
        'Salary 💰', 'Demand 📈', 'Environment 🌍', 'Soft Skills 🤝',
        'Study Duration ⏳', 'Industries 🏭', 'Job Titles 🧾',
        'Traits 😎', 'Certifications 📜', 'Work Hours ⏰'
    ]
    filtered_df_display = filtered_df_display[columns_to_display]
    filtered_df_display.columns = columns_renamed

    st.markdown("<div class='dataframe-style fadeIn'>", unsafe_allow_html=True)
    st.dataframe(filtered_df_display, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

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

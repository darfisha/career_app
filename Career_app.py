import streamlit as st
import pandas as pd
import base64
from io import BytesIO

# Load the dataset
df = pd.read_excel("career_data.xlsx")

# Preprocess skills for consistent matching
df['required_skills'] = df['required_skills'].apply(lambda x: [skill.strip().lower() for skill in x.split(',')])

# Title
st.title("🎯 Career Suggester")
st.markdown("##### Find your ideal career based on your interests and strengths!")

# --- Stream Selection ---
stream_map = {
    "🔬 Science": "Science",
    "💼 Commerce": "Commerce",
    "🎨 Arts/Humanities": "Arts",
    "❓ Not Sure": "Not Sure"
}

st.markdown("### 🎓 Select Your Stream")
stream_choice = st.radio("Choose your stream:", list(stream_map.keys()), horizontal=True)
selected_stream = stream_map[stream_choice]

# --- Skill Selection ---
# Get all unique skills
all_skills = sorted({skill.strip().lower() for skills in df['required_skills'] for skill in skills})

# Emoji mapping for some common skills
emoji_skills = {
    "programming": "💻", "leadership": "🧑‍💼", "communication": "🗣️",
    "creativity": "🎨", "data analysis": "📊", "problem solving": "🧠",
    "teaching": "📚", "empathy": "❤️", "law": "⚖️", "biology": "🧬",
    "teamwork": "🤝", "research": "🔍"
}

skill_display = [f"{emoji_skills.get(skill, '')} {skill.title()}" for skill in all_skills]
skill_map = dict(zip(skill_display, all_skills))

st.markdown("### 🛠️ Select Your Skills")
selected_skills_display = st.multiselect("Choose skills that describe you:", options=skill_display)
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

# Format results for display
if not filtered_df.empty:
    st.markdown("### 🔍 Career Suggestions")
    filtered_df_display = filtered_df.copy()
    filtered_df_display['required_skills'] = filtered_df_display['required_skills'].apply(lambda x: ", ".join([skill.title() for skill in x]))
    filtered_df_display.columns = ['Career 👩‍💼', 'Required Skills 🛠️', 'Stream 🎓', 'Exams 📝']
    st.dataframe(filtered_df_display)

    # Download button (CSV)
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df_display)
    st.download_button("📥 Download as CSV", csv, "career_suggestions.csv", "text/csv")
else:
    st.info("No matching careers found. Try adjusting your stream or skills.")

# --- Reset Button ---
if st.button("🔄 Reset"):
    st.experimental_rerun()

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made with ❤️ by Darfisha Shaikh for Hack the Haze</div>", unsafe_allow_html=True)

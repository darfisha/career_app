import streamlit as st
import pandas as pd
from streamlit_extras.timeline import timeline
import time

# --- Sample Data (replace with your actual dataframe read from CSV) ---
data = [
    {
        "Career": "Data Scientist",
        "Stream": "Science",
        "Required Skills": "Programming, Data Analysis, Machine Learning",
        "Exams": "JEE, GATE, CUET",
        "Education Level Required": "BSc/MSc in Computer Science or related fields",
        "Salary Range (INR/year)": "₹8L - ₹25L",
        "Work Environment": "Remote, Office, Hybrid",
        "Related Industries": "IT, Finance, Healthcare",
        "Typical Job Titles": "Data Scientist, ML Engineer, Data Analyst",
        "Personality Traits": "Analytical, Curious, Problem Solver"
    },
    {
        "Career": "IAS Officer",
        "Stream": "Arts",
        "Required Skills": "Leadership, Critical Thinking, Communication",
        "Exams": "UPSC Civil Services Exam",
        "Education Level Required": "Graduate degree in any discipline",
        "Salary Range (INR/year)": "₹6L - ₹12L",
        "Work Environment": "Office, Field Work",
        "Related Industries": "Government, Public Administration",
        "Typical Job Titles": "IAS Officer, Collector, Administrator",
        "Personality Traits": "Empathetic, Decisive, Ethical"
    },
    {
        "Career": "Chartered Accountant",
        "Stream": "Commerce",
        "Required Skills": "Accounting, Analytical Thinking, Ethics",
        "Exams": "CA Foundation, IPCC, CA Final",
        "Education Level Required": "Commerce Graduate or Equivalent",
        "Salary Range (INR/year)": "₹5L - ₹20L",
        "Work Environment": "Office, Corporate",
        "Related Industries": "Finance, Auditing, Taxation",
        "Typical Job Titles": "CA, Auditor, Financial Analyst",
        "Personality Traits": "Detail-oriented, Responsible, Logical"
    }
]

df = pd.DataFrame(data)

# --- Functions ---
def create_roadmap(career_info):
    roadmap_data = [
        {"time": "Step 1", "title": "🎯 Career", "content": career_info.get("Career", "N/A")},
        {"time": "Step 2", "title": "📚 Exams to Prepare", "content": career_info.get("Exams", "N/A")},
        {"time": "Step 3", "title": "🛠️ Required Skills", "content": career_info.get("Required Skills", "N/A")},
        {"time": "Step 4", "title": "🎓 Education Needed", "content": career_info.get("Education Level Required", "N/A")},
        {"time": "Step 5", "title": "💸 Salary Range (INR/year)", "content": career_info.get("Salary Range (INR/year)", "N/A")},
        {"time": "Step 6", "title": "🌐 Work Environment", "content": career_info.get("Work Environment", "N/A")},
        {"time": "Step 7", "title": "🏢 Related Industries", "content": career_info.get("Related Industries", "N/A")},
        {"time": "Step 8", "title": "🧑‍💼 Typical Job Titles", "content": career_info.get("Typical Job Titles", "N/A")},
        {"time": "Step 9", "title": "🧠 Personality Traits", "content": career_info.get("Personality Traits", "N/A")},
    ]
    return roadmap_data

def staggered_timeline_display(roadmap_data):
    st.markdown("### 🛤️ Career Roadmap")
    # We will show steps one-by-one with delay
    for step in roadmap_data:
        timeline(pd.DataFrame([step]), "time", "title", "content")
        time.sleep(1)  # 1 second delay

# --- Streamlit Layout ---
st.set_page_config(page_title="Find Your Future | AI Career Guide 🇮🇳", layout="centered")

st.title("Find Your Future 🔮 | AI-Powered Career Guide for Indian Students 🇮🇳")
st.write("Let AI help you find where you truly belong... 🎓📊💻🚀")

# User inputs
stream = st.selectbox("What’s your academic stream? 🔬💰🎨", ["Science", "Commerce", "Arts"])
aspiration = st.text_input("What’s your dream career or aspiration? (e.g., IAS Officer, Lawyer, Data Scientist)")

if st.button("🚀 Show Me My Career Path!"):
    # Filter dataset by stream and keyword match in Career column
    filtered = df[
        (df["Stream"].str.lower() == stream.lower()) &
        (df["Career"].str.lower().str.contains(aspiration.strip().lower()))
    ]
    
    if filtered.empty:
        st.warning("😕 Sorry, no career found matching your input. Please try another.")
    else:
        # Pick first match (or you can let user choose if multiple)
        career_info = filtered.iloc[0].to_dict()

        # Celebration animation (confetti)
        st.balloons()
        st.success(f"Found your career path: {career_info['Career']}! 🎉")

        roadmap = create_roadmap(career_info)
        staggered_timeline_display(roadmap)

        # Motivational quote footer
        st.markdown("---")
        st.markdown(
            "✨ **Keep believing in yourself, stay curious, and your dreams will turn into reality!** 💪🌟"
        )

# Reset button
if st.button("🔁 Try Again"):
    st.experimental_rerun()

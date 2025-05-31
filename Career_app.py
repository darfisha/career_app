import streamlit as st
import pandas as pd
import time
from streamlit_lottie import st_lottie
import requests

# --- Load Lottie JSON from URL ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load your dataset ---
@st.cache_data
def load_data():
    # Replace this with your actual dataset path
    df = pd.read_excel('career_data.xlsx')
    # Drop unnecessary columns
    df = df.drop(columns=['Certifications', 'Typical Work Hours'], errors='ignore')
    return df

df = load_data()

# --- Page config ---
st.set_page_config(page_title="Find Your Future 🔮 | AI Career Guide 🇮🇳", layout="centered")

# --- Background image CSS ---
page_bg_img = '''
<style>
body {
  background-image: url("background.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  color: #333;
}
.stApp {
  background: rgba(255, 255, 255, 0.85);
  padding: 2rem 2rem 3rem 2rem;
  border-radius: 10px;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Welcome Lottie animation ---
lottie_welcome = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jbrw3hcz.json")  # fun waving animation

st_lottie(lottie_welcome, height=150, key="welcome")

# --- Header ---
st.title("Find Your Future 🔮 | AI-Powered Career Guide for Indian Students 🇮🇳")
st.markdown("Let AI help you find where you truly belong... 🎓📊💻🚀")

# --- User Input Section ---
stream_choice = st.selectbox("What’s your academic stream? 🔬💰🎨", options=["Science", "Commerce", "Arts"])
dream_career = st.text_input("What’s your dream career or aspiration? (e.g., IAS Officer, Lawyer, Data Scientist)")

if st.button("🚀 Show Me My Career Path!"):
    # Filter dataframe based on stream and partial match in career
    filtered_df = df[
        (df['Stream'].str.lower() == stream_choice.lower()) &
        (df['Career'].str.lower().str.contains(dream_career.lower()))
    ]

    if filtered_df.empty:
        st.error("Sorry, no career found matching your input. Try different keywords or stream.")
    else:
        # Just take first match for simplicity
        career_info = filtered_df.iloc[0]

        # Celebration Lottie
        lottie_celebration = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_touohxv0.json")  # confetti celebration
        st_lottie(lottie_celebration, height=150, key="celebration")

        # Show career name big and bold
        st.markdown(f"## 🎯 {career_info['Career']}")

        # Define roadmap steps
        steps = [
            ("📝 Exams to Prepare For", career_info['Exams']),
            ("🛠️ Required Skills", career_info['Required Skills']),
            ("🎓 Education Needed", career_info['Education Level Required']),
            ("💸 Salary Range in India", career_info['Salary Range (INR/year)']),
            ("🌐 Work Environment", career_info['Work Environment']),
            ("🏢 Industries You’ll Work In", career_info['Related Industries']),
            ("🧑‍💼 Typical Job Titles", career_info['Typical Job Titles']),
            ("🧠 Personality Traits That Fit This Role", career_info['Personality Traits']),
        ]

        # Animated roadmap display
        for i, (title, content) in enumerate(steps, 1):
            st.markdown(f"### Step {i}: {title}")
            st.write(content)
            time.sleep(1)  # 1 second delay for animation effect

        # Motivational message
        st.markdown("""
        ---
        💡 **Remember:** Your journey is unique and filled with endless possibilities. 
        Stay curious, work hard, and believe in yourself! The future belongs to you. 🚀✨
        """)

        # Try again button to reset inputs
        if st.button("🔁 Try Again"):
            st.experimental_rerun()

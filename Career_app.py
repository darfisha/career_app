import streamlit as st
import pandas as pd
import time
import base64

# --- Page Config ---
st.set_page_config(
    page_title="Find Your Future: India’s AI Career Guide 🇮🇳✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Background Image ---
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80");
             background-attachment: fixed;
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

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

        # Animated reveal function
        def reveal_section(title, content, delay=1.0):
            st.markdown(f"### {title}")
            st.markdown(f"{content}")
            time.sleep(delay)

        # Reveal sections one by one with delay
        reveal_section("🎯 Career Name", f"**{career_info['Career']}**")
        reveal_section("📚 Exams to Prepare For", career_info['Exams'])
        reveal_section("🛠️ Required Skills", ", ".join(career_info['Required Skills']))
        reveal_section("🎓 Education Needed", career_info['Education Level Required'])
        reveal_section("💸 Salary Range (INR/year)", career_info['Salary Range (INR/year)'])
        reveal_section("🌐 Work Environment", career_info['Work Environment'])
        reveal_section("🏢 Related Industries", career_info['Related Industries'])
        reveal_section("🧑‍💼 Typical Job Titles", career_info['Typical Job Titles'])
        reveal_section("🧠 Personality Traits That Fit This Role", career_info['Personality Traits'])

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

# careercompass_app.py

import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_excel("career_data.xlsx")

# --- Sidebar Navigation ---
st.sidebar.page_link("Page 1: Find My Career Path 🔍")
st.sidebar.page_link("Page 2: Explore All Careers 📚")

# --- Page Routing Logic ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Page 1: Career Recommendation ---
def find_my_career():
    st.title("Find My Career Path 🔍")
    st.markdown("Choose your preferences below and get career recommendations! 🧠")

    stream = st.radio("Select your stream 🎓", ["Science", "Commerce", "Arts", "Not Sure"])

    hard_skills = ["💻 Programming", "📊 Data Analysis", "📐 Design Thinking", "📚 Research", "📈 Financial Analysis"]
    soft_skills = ["🗣️ Communication", "🤝 Teamwork", "🧠 Problem-Solving", "💡 Creativity", "⏰ Time Management"]

    selected_skills = st.multiselect("Select your skills ✨", hard_skills + soft_skills)

    exam_input = st.text_input("Enter any exams you're interested in or have taken (optional) 📝")

    if st.button("🎯 Get Career Recommendations"):
        filtered_df = df.copy()

        if stream != "Not Sure":
            filtered_df = filtered_df[filtered_df['Stream'].str.contains(stream)]

        if selected_skills:
            for skill in selected_skills:
                skill_clean = skill.split(" ")[1] if " " in skill else skill
                filtered_df = filtered_df[filtered_df['Required Skills'].str.contains(skill_clean, case=False)]

        if exam_input:
            filtered_df = filtered_df[filtered_df['Exams'].str.contains(exam_input, case=False)]

        st.subheader("🔎 Recommended Careers")
        if not filtered_df.empty:
            for _, row in filtered_df.iterrows():
                with st.container():
                    st.markdown(f"### 💼 {row['Career']}")
                    st.markdown(f"**Salary:** ₹{row['Salary Range (INR/year)']}")
                    st.markdown(f"**Exams:** {row['Exams']}")
                    st.markdown(f"**Skills:** {row['Required Skills']}")
                    st.markdown(f"**Demand:** 🔥 {row['Job Demand']}")
                    st.markdown("---")

            st.download_button("📥 Download Recommendations as CSV", data=filtered_df.to_csv(index=False), file_name="career_recommendations.csv")
        else:
            st.info("No careers matched your selection. Try different filters! 🙏")

        if st.button("🔄 Reset Filters"):
            st.experimental_rerun()

# --- Page 2: Explore All Careers ---
def explore_all():
    st.title("Explore All Careers 📚")
    st.markdown("Search, filter, and discover all available career options! 🧭")

    stream_filter = st.selectbox("Filter by stream 🎓", ["All"] + df['Stream'].unique().tolist())
    exam_filter = st.text_input("Filter by exam ✍️")
    skill_filter = st.text_input("Filter by skill 🛠️")
    trait_filter = st.text_input("Filter by personality trait 🌟")

    filtered_df = df.copy()
    if stream_filter != "All":
        filtered_df = filtered_df[filtered_df['Stream'] == stream_filter]
    if exam_filter:
        filtered_df = filtered_df[filtered_df['Exams'].str.contains(exam_filter, case=False)]
    if skill_filter:
        filtered_df = filtered_df[filtered_df['Required Skills'].str.contains(skill_filter, case=False)]
    if trait_filter:
        filtered_df = filtered_df[filtered_df['Personality Traits'].str.contains(trait_filter, case=False)]

    st.dataframe(filtered_df, use_container_width=True)

    st.caption("⭐ Click the star icon to save favorites (session only)")

    st.markdown("---")
    st.markdown("Made with ❤️ by Darfisha Shaikh for Hack the Haze 🚀")

# --- Page Selection Logic ---
page = st.sidebar.radio("Navigate", ["Find My Career Path 🔍", "Explore All Careers 📚"])
if page == "Find My Career Path 🔍":
    find_my_career()
elif page == "Explore All Careers 📚":
    explore_all()

import streamlit as st
import openai

# OpenAI config
openai.api_key = st.secrets["api_key"]

# Streamlit layout settings
st.set_page_config(page_title="Exercise Generator", layout="wide")

# Streamlit app layout
st.title(":green[Adaptive Exercise] Generator :mortar_board:")

# App description
st.subheader(
    ":sparkles: A demonstration of Generative AI's capabilities in Adaptive Learning.:sparkles:",
    divider="green",
)
st.markdown(
    """*Select a **language** for the generated exercise, the student **grade**, provide the **student's previous marks**, and select a **subject**.  
        Click on the **Generate Exercise** button to get an adapted exercise tailored to challenge students according to their skill level.*
"""
)

# Add selects to the sidebar:
language = st.sidebar.selectbox("Output Language", ("English", "French"))
grade = st.sidebar.selectbox(
    "Grade (EN - FR)",
    (
        "4th Grade - CM1",
        "8th Grade - 4ème",
        "12th Grade - Terminale",
    ),
)
marks = st.sidebar.selectbox(
    "Previous Marks",
    (
        "Student A (C, C, C, D)",
        "Student B (B, A, C, D)",
        "Student C (A, B, A, A)",
        "Student D (A, A, A, A)",
    ),
)
subject = st.sidebar.selectbox(
    "Subject",
    (
        "Grammar",
        "Vocabulary",
        "Reading Comprehension",
        "Writing",
        "Algebra",
        "Geometry",
    ),
)

# Button to generate exercise
if st.sidebar.button("Generate Exercise"):
    if subject == "Language":
        if language == "English":
            subject = "English"
        elif language == "French":
            subject = "French"
        else:
            subject = "English"

    prompt = f"""
You are a helpful instructional coach assisting teachers in lesson planning. 
Your task is to create a top-notch exercise to enhance a student's skills. 
You have access to the student's prior marks, their current grade, and the subject. 
Given this information, generate a {subject} exercise for the {grade} level, tailored to the student's previous performance: {marks}.
Your exercise should encompass the following elements:
-Title
-Exercise
-Answers
-Targeted Learning Objectives
-Adaptation to Prior Student Performance
Compose the entire response in {language}.
"""

    # Make an API call to Chat-GPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    if completion:
        exercise = completion["choices"][0]["message"]["content"]
        # Display the generated exercise and feedback
        st.subheader("Generated Exercise :")
        st.write(exercise)
    else:
        st.error("Error generating the exercise. Please try again.")

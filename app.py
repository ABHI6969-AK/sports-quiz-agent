import streamlit as st
import json
from src.database import retrieve_context
from src.search import search_web
from src.generator import generate_quiz

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Sports Quiz",
    page_icon="🏆",
    layout="wide"
)

# ---------------- LOAD CSS ----------------

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("# 🏆 AI Sports Quiz")

    st.markdown("---")

    st.metric("Questions", "5")

    st.metric("AI Model", "Groq")

    st.metric("Database", "ChromaDB")

    st.markdown("---")

    st.info(
        """
Generate quizzes powered by

✅ AI

✅ RAG

✅ Latest Sports News
"""
    )

# ---------------- HEADER ----------------

st.markdown(
    """
<div class='title'>
🏆 AI Sports Quiz Generator
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class='subtitle'>
Powered by Groq • ChromaDB • RAG • DuckDuckGo
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------

col1, col2 = st.columns(2)

with col1:

    sport = st.selectbox(
        "⚽ Choose Sport",
        [
            "Cricket",
            "Football",
            "Tennis"
        ]
    )

with col2:

    difficulty = st.selectbox(
        "🎯 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- GENERATE ----------------

if st.button("🚀 Generate AI Quiz", use_container_width=True):

    with st.spinner("🤖 AI is generating your quiz..."):

        db = retrieve_context(sport)

        news = search_web(f"Latest {sport} news")

        context = "\n".join(db + news)

        quiz = generate_quiz(
            sport,
            difficulty,
            context,
        )

        if isinstance(quiz, str):
            quiz = json.loads(quiz)

        st.session_state.quiz = quiz
        st.session_state.answers = {}
        st.session_state.submitted = False

    st.success("Quiz Generated Successfully!")

# ---------------- SHOW QUIZ ----------------

if st.session_state.quiz:

    st.markdown("---")

    total_questions = len(st.session_state.quiz)

    for i, question in enumerate(st.session_state.quiz):

        st.markdown(
            f"""
<div class='card'>
<h3>Question {i+1} of {total_questions}</h3>
<p style='font-size:20px;'>{question["question"]}</p>
</div>
""",
            unsafe_allow_html=True,
        )

        selected = st.radio(
            "Choose your answer",
            question["options"],
            key=f"question_{i}",
        )

        st.session_state.answers[i] = selected

        st.markdown("<br>", unsafe_allow_html=True)

    progress = len(st.session_state.answers) / total_questions
    st.progress(progress)

    if st.button("✅ Submit Quiz", use_container_width=True):

        score = 0

        st.markdown("---")
        st.header("🏆 Quiz Results")

        for i, question in enumerate(st.session_state.quiz):

            user_answer = st.session_state.answers.get(i)
            correct_answer = question["answer"]

            if user_answer == correct_answer:

                score += 1

                st.success(
                    f"Question {i+1}: Correct"
                )

            else:

                st.error(
                    f"Question {i+1}: Incorrect"
                )

                st.info(
                    f"Correct Answer: {correct_answer}"
                )

        st.markdown("---")

        percentage = (score / total_questions) * 100

        st.metric(
            "Final Score",
            f"{score}/{total_questions}",
            f"{percentage:.0f}%"
        )

        if percentage >= 80:

            st.balloons()

            st.success(
                "🌟 Excellent Performance!"
            )

        elif percentage >= 60:

            st.success(
                "👏 Good Job!"
            )

        else:

            st.warning(
                "💪 Keep Practicing!"
            )

        if st.button(
            "🔄 Play Again",
            use_container_width=True
        ):

            st.session_state.quiz = None
            st.session_state.answers = {}

            st.rerun()
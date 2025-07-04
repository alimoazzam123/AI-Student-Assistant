import streamlit as st
from euriai import EuriaiLangChainLLM
from euriai.langchain_embed import EuriaiEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os
import re
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def parse_questions(raw_text):
    questions = re.split(r'\n(?=\d+\.)', raw_text.strip())
    parsed = []
    for q in questions:
        if not q.strip():
            continue
        lines = q.strip().split("\n")
        question_text = lines[0].strip()

        options = []
        correct = None

        for line in lines[1:]:
            line = line.strip()
            if line.lower().startswith("answer"):
                match = re.search(r"Answer[:\-]?\s*([A-D])", line, re.IGNORECASE)
                if match:
                    correct = match.group(1).upper()
            elif re.match(r"[A-D]\)", line):  # A) B) etc.
                options.append(line)

        parsed.append({
            "question": question_text,
            "options": options,
            "correct": correct
        })

    return parsed

def quiz_generator():
    st.header("📝 Quiz Generator")

    selected_model = st.session_state.get("llm_model", "gpt-4.1-nano")
    uploaded_pdf = st.session_state.get("pdf_docs", None)

    # Model setup
    llm = EuriaiLangChainLLM(
        api_key=API_KEY,
        model=selected_model,
        temperature=0.7,
        max_tokens=500
    )

    # Options
    option = st.radio("How would you like to generate the quiz?", ["🔤 From LLM", "📄 From Books"])
    topic = st.text_input("📘 Enter topic or concept:")
    num_questions = st.slider("🧮 Number of questions", 1, 10, 5)

    if st.button("🚀 Generate Quiz"):
        if not topic.strip():
            st.warning("⚠️ Please enter a topic before generating the quiz.")
            return

        with st.spinner("Generating quiz..."):

            if option == "📄 From Books":
                if not uploaded_pdf:
                    st.warning("📄 Please upload a PDF in the sidebar first.")
                    return
                embeddings = EuriaiEmbeddings(api_key=API_KEY)
                vectorstore = FAISS.load_local(
                    "vector_store",
                    embeddings=embeddings,
                    allow_dangerous_deserialization=True
                )
                retriever = vectorstore.as_retriever()
                docs = retriever.get_relevant_documents(topic)
                context = "\n".join(doc.page_content for doc in docs)

                prompt = (
                    f"Generate {num_questions} multiple-choice questions on the topic: '{topic}' "
                    f"based on the following context from a book:\n\n{context[:4000]}\n\n"
                    "Each question must have 4 options (A-D), and provide answer as 'Answer: A/B/C/D'"
                )

            else:
                # From LLM
                prompt = (
                    f"Generate {num_questions} multiple-choice questions on the topic: '{topic}'.\n"
                    "Each question must have 4 options (A-D) and include the correct answer at the end like 'Answer: B'."
                )

            try:
                result = llm.invoke(prompt)
                parsed_quiz = parse_questions(result)

                if not parsed_quiz:
                    st.error("⚠️ Unable to parse quiz. Try refining your topic.")
                    return

                st.session_state.quiz = parsed_quiz
                st.session_state.answers = {}
                st.session_state.submitted = False
                st.success("✅ Quiz generated successfully!")

            except Exception as e:
                st.error(f"🚫 Failed to generate quiz: {e}")
                return

    if "quiz" in st.session_state and not st.session_state.get("submitted", False):
        for idx, q in enumerate(st.session_state.quiz):
            st.markdown(f"**Q{idx+1}: {q['question']}**")
            st.session_state.answers[idx] = st.radio(
                f"Choose your answer",
                q["options"],
                key=f"q{idx}"
            )
            st.markdown("---")

        if st.button("✅ Submit Answers"):
            st.session_state.submitted = True

    if st.session_state.get("submitted", False):
        score = 0
        st.subheader("📊 Your Results")
        for idx, q in enumerate(st.session_state.quiz):
            selected = st.session_state.answers.get(idx)
            correct_letter = q["correct"]
            correct_option = next((opt for opt in q["options"] if opt.strip().startswith(correct_letter)), None)

            if correct_letter and selected and selected.strip().startswith(correct_letter):
                st.success(f"✅ Q{idx+1}: Correct")
                score += 1
            else:
                st.error(f"❌ Q{idx+1}: Incorrect")
                if correct_option:
                    st.markdown(f"**✔️ Correct Answer:** {correct_option}**")
                else:
                    st.warning("⚠️ Correct answer not found.")

            st.markdown("---")

        st.success(f"🎯 Your Score: **{score}/{len(st.session_state.quiz)}**")

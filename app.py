import streamlit as st
from src.components.doubt_solver import doubt_solver
from src.components.quiz_generator import quiz_generator
from src.components.roadmap_creator import roadmap_generator
from src.utils.ingest import generate_vector_store
import os

# Set page config
st.set_page_config(page_title="AI Student Assistant", layout="wide")


# Sidebar UI
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("🚀 AI Student Assistant")

# Feature Selection
option = st.sidebar.selectbox("Choose Feature", ("🏠 Home", "📖 Doubt Solver", "📝 Quiz Generator", "🧭 Roadmap Creator"))

# Model Selection
model = st.sidebar.selectbox(
    "🧠 Choose your AI model:",
    [
        "gpt-4.1-nano",
        "gpt-4.1-mini",
        "gemini-2.0-flash",
        "llama-4-maverick-17b-128e-instruct",
        "mistral-saba-24b",
        "deepseek-r1-distill-llama-70b"
    ]
)
st.session_state.llm_model = model

# Initialize PDF and vector store status
if "pdf_docs" not in st.session_state:
    st.session_state.pdf_docs = None

if "vector_ready_for" not in st.session_state:
    st.session_state.vector_ready_for = None  # path of last embedded PDF

# PDF Upload & Conditional Vector Generation
uploaded_file = st.sidebar.file_uploader("📄 Upload your Study Material (PDF)", type="pdf")

if uploaded_file:
    os.makedirs("pdfs", exist_ok=True)
    save_path = f"pdfs/{uploaded_file.name}"

    # Save PDF to local path
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    st.session_state.pdf_docs = save_path

    # Only generate vector store if this PDF is new
    if st.session_state.vector_ready_for != save_path:
        with st.spinner("🔄 Creating vector store from your new PDF..."):
            generate_vector_store(save_path)
        st.session_state.vector_ready_for = save_path
        st.success("✅ Vector store created successfully!")

# Main Container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Home Page
if option == "🏠 Home":
    st.title("🌟 Welcome to AI Student Assistant")

    st.markdown("""
        <h2>📚 Unlock Your Academic Potential with Smart AI Tools</h2>
        <p style="color: #444;">Explore the powerful tools integrated into this assistant designed to support your learning journey.</p>
        <hr style="margin: 1rem 0;">
        <h3>🧠 Features:</h3>

        <div style="line-height: 1.8; font-size: 16px;">
            <ul> 
                <li>
                    <strong>📖 Doubt Solver:</strong> Ask questions directly from your uploaded book using state-of-the-art Retrieval-Augmented Generation (RAG).<br>
                    <em>🔍 Ideal for clearing concepts from textbooks and PDFs in real-time.</em>
                </li>
                <li>
                    <strong>📝 Quiz Generator:</strong> Instantly generate multiple-choice questions from any topic or chapter of your PDF.<br>
                    <em>🎯 Great for self-assessment, revision, and practice before exams.</em>
                </li>
                <li>
                    <strong>🧭 Roadmap Creator:</strong> Create a week-by-week learning roadmap based on your selected topic and skill level (Beginner/Advanced).<br>
                    <em>📅 Perfect for structured learning with curated resources and motivational tips.</em>
                </li>
                <li>
                    <strong>🤖 Model Selection:</strong> Choose from a variety of top-tier LLMs like GPT-4.1, Gemini, LLaMA, DeepSeek, and more.<br>
                    <em>⚙️ Use different models based on speed, reasoning power, or multilingual capabilities.</em>
                </li>
                <li>
                    <strong>📂 Unified Document Upload:</strong> Upload a single PDF that powers all tools — doubt solving, quiz generation, and roadmap planning.<br>
                    <em>💡 Simplifies your workflow and keeps all features in sync.</em>
                </li>
            </ul>
        </div>

        <br><hr style="margin: 1.5rem 0;">
        <p style="color: #333; font-size: 15px;">
            Ready to begin? Upload your study material in the sidebar, choose a feature, and let AI boost your productivity! 🚀
        </p>
    """, unsafe_allow_html=True)

# Feature Routing
elif option == "📖 Doubt Solver":
    if st.session_state.pdf_docs:
        doubt_solver()
    else:
        st.warning("📄 Please upload a PDF document from the sidebar first.")

elif option == "📝 Quiz Generator":
    if st.session_state.pdf_docs:
        quiz_generator()
    else:
        st.warning("📄 Please upload a PDF document from the sidebar first.")

elif option == "🧭 Roadmap Creator":
    roadmap_generator(model=st.session_state.llm_model)

st.markdown("</div>", unsafe_allow_html=True)



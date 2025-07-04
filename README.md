# 🎓 AI Student Assistant  
**Your Personalized Learning Buddy — Powered by AI + Streamlit + RAG**

📚 Get answers, quizzes, and a personalized study roadmap — all from your own study material.  
Boost your learning experience with this all-in-one AI academic assistant built just for students like you.
## 🚀 Features at a Glance

| 💡 Feature              | 📘 Description |
|-------------------------|----------------|
| 📖 **Doubt Solver**     | Ask any question from your uploaded study PDF and get accurate answers powered by Retrieval-Augmented Generation (RAG). |
| 📝 **Quiz Generator**   | Instantly create topic-based multiple-choice quizzes with correct answers from either your document or AI context. |
| 🧭 **Roadmap Creator**  | Generate a customized weekly learning roadmap based on your topic, duration, and skill level. |
| 🤖 **Dynamic Model Selection** | Choose your preferred LLM from GPT-4.1, Gemini, LLaMA, Mistral, DeepSeek, and more. |
| 📂 **Unified PDF Upload** | Upload your study material once and use it across all features — no repeated uploads. |

---

## 🧠 Built With

- **Streamlit** – Interactive Web UI  
- **EuriaiLangChainLLM** – Access to powerful models like GPT, Gemini, LLaMA  
- **FAISS + LangChain** – Vector store & RAG-powered document search  
- **PyMuPDF** – PDF parsing and processing  
- **Euriai Embeddings** – For vector generation

---

## 🔧 Getting Started

### 1️⃣ Clone the Project

```bash
git clone https://github.com/alimoazzam123/ai-student-assistant.git
cd ai-student-assistant


###2️⃣ Create and Activate Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

###3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
###4️⃣ Add API Key
Create a .env file and add your EURI AI key:

env
Copy
Edit
API_KEY=your_euriai_api_key
5️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
Visit: http://localhost:8501

📁 File Structure
bash
Copy
Edit
📦 ai-student-assistant
├── app.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies
├── .env                         # API key file
├── assets/                      # Logo & background
├── pdfs/                        # Uploaded PDFs
├── vector_store/                # FAISS vector DB
└── src/
    └── components/
        ├── doubt_solver.py
        ├── quiz_generator.py
        └── roadmap_creator.py
🖼️ Sample Screenshots (optional)
Add your own screenshots from the app UI (Home, Quiz, Doubt Solver, Roadmap)

🔮 Coming Soon
🧑‍🏫 Homework Checker

📈 Learning Analytics

🗣️ Multilingual Query Support

🧠 AI Tutor Agent

📅 Study Scheduler

👨‍💻 Author
Md Moazzam Ali
📧 moazzam@example.com
🔗 LinkedIn

📄 License
This project is licensed under the MIT License.
You’re free to use, modify, and distribute for educational or personal use.

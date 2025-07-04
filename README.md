🎓 AI Student Assistant
Your Personalized Learning Buddy — Powered by AI + Streamlit + RAG

📚 Get answers, quizzes, and a personalized study roadmap — all from your own study material.
Boost your learning experience with this all-in-one AI academic assistant built just for students like you.

</div>
🚀 Features at a Glance
💡 Feature	📘 Description
📖 Doubt Solver	Ask any question from your uploaded study PDF and get accurate answers powered by Retrieval-Augmented Generation (RAG).
📝 Quiz Generator	Instantly create topic-based multiple-choice quizzes with correct answers from either your document or AI context.
🧭 Roadmap Creator	Generate a customized weekly learning roadmap based on your topic, duration, and skill level.
🤖 Dynamic Model Selection	Choose your preferred LLM from GPT-4.1, Gemini, LLaMA, Mistral, DeepSeek, and more.
📂 Unified PDF Upload	Upload your study material once and use it across all features — no repeated uploads.

🧠 Built With
Streamlit – Interactive Web UI

EuriaiLangChainLLM – Access to powerful models like GPT, Gemini, LLaMA

FAISS + LangChain – Vector store & RAG-powered document search

PyMuPDF – PDF parsing and processing

Euriai Embeddings – For vector generation

🔧 Getting Started
1️⃣ Clone the Project
bash
Copy
Edit
git clone https://github.com/alimoazzam123/ai-student-assistant.git
cd ai-student-assistant
2️⃣ Set Up Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Add Your Euriai API Key
Create a .env file and paste:

env
Copy
Edit
API_KEY=your_euriai_api_key
5️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
Once started, open in your browser: http://localhost:8501

📁 Project Structure
bash
Copy
Edit
├── app.py                       # Main Streamlit app with routing
├── requirements.txt             # List of Python dependencies
├── .env                         # Hidden file with API key
├── assets/                      # Logo and background
├── pdfs/                        # Uploaded study PDFs
├── vector_store/                # Auto-generated FAISS vector DB
└── src/
    └── components/
        ├── doubt_solver.py
        ├── quiz_generator.py
        └── roadmap_creator.py
📸 Screenshots (Optional)
Coming soon! Include screenshots of home, doubt solver, quiz, and roadmap.

🔮 What’s Next?
📑 Homework Checker (PDF/text analysis)

📉 Progress Tracker

✨ Text Summarizer

🌐 Multilingual Support

🧑‍🏫 AI-based Teaching Agent

👨‍💻 Author
Md Moazzam Ali
📬 mdmoazzamali984@gmail.com
🔗 LinkedIn

📄 License
This project is licensed under the MIT License.
Feel free to modify or enhance for educational or personal use.

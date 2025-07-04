# 🎓 AI Student Assistant  
*Your Personalized Learning Buddy — Powered by AI, Streamlit, and LangChain*  

📚 Upload your study material once and unlock:  
📖 Smart doubt solving | 📝 Auto-generated quizzes | 🧭 Personalized learning roadmaps  

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📖 **Doubt Solver** | Ask any question directly from your uploaded PDF using Retrieval-Augmented Generation (RAG) with top-tier LLMs. |
| 📝 **Quiz Generator** | Create MCQs from the uploaded PDF or generate them directly from your prompt/topic. |
| 🧭 **Roadmap Creator** | Build a weekly roadmap to master any topic, tailored to your skill level and duration. |
| 🤖 **Dynamic Model Selection** | Choose from top-performing AI models like `gpt-4.1-nano`, `gemini-2.0-flash`, `llama-4`, `deepseek`, and more. |
| 📂 **Unified PDF Usage** | Upload your study material once and use it across all features without re-uploading. |

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **AI/LLM**: Euriai API (GPT, Gemini, LLaMA, etc.)  
- **Embeddings**: Euriai Embeddings  
- **Vector DB**: FAISS  
- **PDF Parsing**: PyMuPDF  
- **Frameworks**: LangChain, dotenv  

---

## 💻 How to Run Locally

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/alimoazzam123/ai-student-assistant.git  
   cd ai-student-assistant
   ```

2. **Create and Activate a Virtual Environment**  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your API Key**  
   Create a `.env` file and add your EURI API key:  
   ```
   API_KEY=your_euriai_api_key_here
   ```

5. **Run the App**  
   ```bash
   streamlit run app.py
   ```  
   Visit [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
ai-student-assistant/
├── app.py                 # Main Streamlit app
├── .env                   # Environment config
├── requirements.txt       # Python dependencies
├── assets/                # Logo, background images
├── pdfs/                  # Uploaded PDFs
├── vector_store/          # FAISS vector index
└── src/components/        # Core feature modules
    ├── doubt_solver.py
    ├── quiz_generator.py
    └── roadmap_creator.py
```

---

## 📊 Example Use Cases

- Students solving doubts directly from uploaded PDFs  
- Teachers preparing quizzes for quick assessments  
- Learners creating smart, weekly roadmaps to master any topic  
- Language learners using multilingual models for assistance  

---

## 👨‍💻 Author

**Md Moazzam Ali**  
📧 mdmoazzamali984@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/mdmoazzamali)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share!





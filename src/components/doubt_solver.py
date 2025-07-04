import streamlit as st
from euriai import EuriaiLangChainLLM
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from euriai.langchain_embed import EuriaiEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def doubt_solver():
    st.header("📖 Doubt Solver")

    API_KEY = os.getenv("API_KEY")
    model_name = st.session_state.get("llm_model", "gpt-4.1-nano")
    pdf_path = st.session_state.get("pdf_docs", None)

    if not pdf_path:
        st.warning("⚠️ Please upload a PDF from the sidebar to use this feature.")
        return

    query = st.text_input("Ask your question from the uploaded book:")

    if query:
        try:
            # Load vectorstore
            vectorstore = FAISS.load_local(
                "vector_store",
                EuriaiEmbeddings(api_key=API_KEY),
                allow_dangerous_deserialization=True
            )
            retriever = vectorstore.as_retriever()

            # Initialize LLM
            llm = EuriaiLangChainLLM(
                api_key=API_KEY,
                model=model_name,
                temperature=0.7,
                max_tokens=300
            )

            # QA Chain
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True
            )

            result = qa_chain.invoke({"query": query})
            st.success(result["result"])

            with st.expander("📄 Source Documents"):
                for doc in result["source_documents"]:
                    page = doc.metadata.get("page", "Unknown")
                    content = doc.page_content.strip()
                    st.markdown(f"📘 **Page {page}**")
                    st.text(content[:500] + "..." if len(content) > 500 else content)
                    st.markdown("---")

        except Exception as e:
            st.error(f"🚫 An error occurred while processing your query: {e}")

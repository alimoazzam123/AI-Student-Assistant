import streamlit as st
from euriai import EuriaiLangChainLLM
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def roadmap_generator(model=None):
    st.title("🧭 Personalized Roadmap Creator")
    st.markdown("Design a custom week-wise learning roadmap based on your goals and experience level. Let’s get started! 🚀")

    # Inputs
    topic = st.text_input("🎯 What topic do you want to master?")
    level = st.selectbox("📊 Select your current proficiency level:", ["Beginner", "Intermediate", "Advanced"])
    weeks = st.slider("📆 Duration of your learning journey (weeks)", min_value=4, max_value=12, value=8)

    # Generate Roadmap
    if st.button("📍 Generate My Roadmap"):
        if not topic:
            st.warning("⚠️ Please enter a topic before generating the roadmap.")
            return

        with st.spinner("⏳ Crafting your learning path..."):

            try:
                llm = EuriaiLangChainLLM(
                    api_key=API_KEY,
                    model=model or st.session_state.get("llm_model", "gpt-4.1-nano"),
                    temperature=0.7,
                    max_tokens=2000
                )

                prompt = f"""
You are an expert education coach. Design a clear, motivating, and week-by-week roadmap to master the topic **"{topic}"** in **{weeks} weeks** for a **{level}** learner.

Follow this format strictly for each week:
Week [Number]: [Catchy Title]
Tasks:
- Task 1
- Task 2
Resources:
- Resource 1
- Resource 2
Motivation:
- Encouragement or advice for the learner

End the roadmap with an inspiring final message to keep learning and growing.

Keep language friendly, structured, and engaging.
                """

                response = llm.invoke(prompt).strip()
                if not response:
                    st.error("⚠️ Empty response received. Try rephrasing the topic.")
                    return

                st.markdown("## 📌 Your Personalized Roadmap")
                week_blocks = response.split("Week ")

                for entry in week_blocks[1:]:
                    header, *body = entry.strip().split("\n", 1)
                    if ":" not in header:
                        continue
                    week_number, title = header.split(":", 1)
                    week_number = week_number.strip()
                    title = title.strip()
                    content = body[0] if body else ""

                    with st.expander(f"🗓️ Week {week_number}: {title}"):
                        st.markdown(
                            content.replace("Tasks:", "**📝 Tasks:**")
                                   .replace("Resources:", "**📚 Resources:**")
                                   .replace("Motivation:", "**💡 Motivation:**")
                        )

            except Exception as e:
                st.error(f"🚫 An error occurred while generating the roadmap:\n`{e}`")

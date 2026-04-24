import streamlit as st
import os
from google import genai
from tavily import TavilyClient

# --- CONFIGURATION ---
# (Replace with your actual keys)
GEMINI_KEY = os.environ.get("GEMINI_KEY")
TAVILY_KEY = os.environ.get("TAVILY_KEY")
if not GEMINI_KEY or not TAVILY_KEY:
    st.error("API Keys missing! Please add GEMINI_KEY and TAVILY_KEY in Railway Variables.")
    st.stop()

client = genai.Client(api_key=GEMINI_KEY)
tavily = TavilyClient(api_key=TAVILY_KEY)

# --- UI INTERFACE ---
st.set_page_config(page_title="AI Exam Generator", page_icon="🧠")

st.title("🧠 AI Exam Generator (FREE VERSION)")

# Input Fields
subject = st.text_input("Subject", placeholder="e.g. Computer Science")
topic = st.text_input("Topic", placeholder="e.g. Cloud Computing and AWS")
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

if st.button("Generate Exam"):
    if not subject or not topic:
        st.error("Please fill in both Subject and Topic!")
    else:
        with st.status("Agent is searching and thinking...", expanded=True) as status:
            try:
                # 1. Research
                st.write("[*] Researching syllabus content...")
                search_query = f"academic syllabus for {topic} in {subject}"
                search_results = tavily.search(query=search_query, search_depth="advanced")
                
                # 2. Generate
                st.write("[*] Generating Exam Questions...")
                gen_prompt = f"Research: {search_results}\n\nGenerate a {difficulty} level exam for {topic} in {subject}. Include 3 MCQs and 2 Short Answers."
                exam_paper = client.models.generate_content(model="gemini-2.5-flash-lite", contents=gen_prompt).text
                
                # 3. Judge
                st.write("[*] Judge Agent is checking quality...")
                judge_prompt = f"Review this exam for {difficulty} level accuracy:\n\n{exam_paper}"
                validation = client.models.generate_content(model="gemini-2.5-flash-lite", contents=judge_prompt).text
                
                status.update(label="Exam Generated!", state="complete", expanded=False)

                # Display Results
                st.subheader("Generated Exam Paper")
                st.markdown(exam_paper)
                
                st.divider()
                st.subheader("Judge Validation Report")
                st.info(validation)

            except Exception as e:
                st.error(f"Error: {e}")
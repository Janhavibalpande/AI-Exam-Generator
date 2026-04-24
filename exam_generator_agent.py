from google import genai
from tavily import TavilyClient

# --- CONFIGURATION ---
GEMINI_KEY = "AIzaSyAPwEMdoG76hE0sx1YmSJZuSMKt_7yPy8M"
TAVILY_KEY = "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"

client = genai.Client(api_key=GEMINI_KEY)
tavily = TavilyClient(api_key=TAVILY_KEY)

def exam_generator_agent(topic):
    # STEP 1: Research Syllabus-level content
    print(f"[*] Researching syllabus content for: {topic}...")
    search_query = f"academic syllabus and key concepts for {topic} 2026"
    search_results = tavily.search(query=search_query, search_depth="advanced")
    context = str(search_results)

    # STEP 2: Generate Questions (MCQs and Short Answers)
    print("[*] Generating Exam Questions...")
    gen_prompt = f"""
    Using this research: {context}
    Generate an exam paper for '{topic}' with the following:
    1. 3 Multiple Choice Questions (MCQs) with 4 options and 1 correct answer.
    2. 2 Short Answer Questions (SAQs).
    3. Include Difficulty Ratings (Easy, Medium, Hard) and a hidden Answer Key.
    Format clearly as a formal exam paper.
    """
    exam_paper = client.models.generate_content(model="gemini-2.5-flash", contents=gen_prompt).text

    # STEP 3: Judge Agent - Validation
    print("[*] Judge Agent is checking clarity and difficulty distribution...")
    judge_prompt = f"""
    Review the following Exam Paper:
    {exam_paper}
    
    Task: 
    - Check for factual correctness.
    - Ensure a mix of difficulty levels (Easy to Hard).
    - Verify that the Answer Key matches the questions.
    Provide a 'Validation Report' and a final 'Approval' status.
    """
    validation = client.models.generate_content(model="gemini-2.5-flash", contents=judge_prompt).text

    # FINAL OUTPUT
    print("\n" + "="*40)
    print(" GENERATED EXAM PAPER ")
    print("="*40)
    print(exam_paper)
    print("\n" + "="*40)
    print(" JUDGE VALIDATION REPORT ")
    print("="*40)
    print(validation)

# --- EXECUTION ---
# You can change this to any subject (e.g., "Data Structures", "Organic Chemistry")
exam_generator_agent("Cloud Computing and AWS Infrastructure")
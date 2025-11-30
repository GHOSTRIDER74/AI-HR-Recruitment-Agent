import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class RecruitmentAgent:
    def __init__(self):
        # Configure the Gemini API
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("API Key not found. Please check your .env file.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def analyze_candidate(self, resume_text, jd_text):
        """
        Sends the resume and JD to Gemini for analysis.
        """
        prompt = f"""
        You are an expert Technical Recruiter with 20 years of experience. 
        Your task is to evaluate a candidate based on a specific Job Description.

        JOB DESCRIPTION:
        {jd_text}

        CANDIDATE RESUME:
        {resume_text}

        ---
        Based on the above, provide a structured analysis in the following format:
        
        1. MATCH SCORE: [0-100]%
        2. DECISION: [Select for Interview / Reject]
        3. KEY STRENGTHS: [List 3 top matching skills/experiences]
        4. MISSING CRITICAL SKILLS: [List major gaps]
        5. REASONING: [A brief 2-sentence summary of why you made this decision]
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error during analysis: {e}"

# --- TEST BLOCK ---
if __name__ == "__main__":
    # Simple test to ensure API is working
    try:
        agent = RecruitmentAgent()
        print("Agent initialized successfully!")
        
        # Dummy data for testing connection
        test_resume = "I have 5 years of Python experience and know SQL."
        test_jd = "Looking for a Python developer with SQL knowledge."
        
        print("\n--- Running Test Analysis ---")
        result = agent.analyze_candidate(test_resume, test_jd)
        print(result)
        
    except Exception as e:
        print(f"Agent failed to start: {e}")
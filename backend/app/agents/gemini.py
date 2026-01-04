import google.generativeai as genai
import os

class GeminiAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Error: GEMINI_API_KEY not found.")
            self.model = None
            return

        genai.configure(api_key=api_key)
        # using the users requested model string
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')

    async def execute(self, prompt: str) -> str:
        if not self.model:
            return "Error: Gemini API Key missing."
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Employee Gemini is currently unreachable. Error: {str(e)}"

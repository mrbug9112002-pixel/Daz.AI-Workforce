import google.generativeai as genai
import os

class GeminiAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Error: GEMINI_API_KEY not found.")
            self.model = None
            return

        # Anti-Gravity Engine: Direct connection to v1.5 Flash
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        print(f"Anti-Gravity Engine initialized with: {self.model.model_name}")

    async def execute(self, prompt: str) -> str:
        if not self.model:
            return "Error: Gemini API Key missing."
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_str = str(e)
            if "404" in error_str or "not found" in error_str.lower():
                # Self-Healing: Switch to gemini-pro and retry
                try:
                    # Fallback to gemini-pro
                    self.model = genai.GenerativeModel('gemini-pro')
                    response = self.model.generate_content(prompt)
                    return response.text
                except Exception as e2:
                     return f"Employee Gemini is unreachable (Fallback failed). Error: {str(e2)}"

            return f"Employee Gemini is currently unreachable. Error: {str(e)}"

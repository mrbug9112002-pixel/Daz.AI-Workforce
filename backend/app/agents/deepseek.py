import os
from openai import AsyncOpenAI

class DeepSeekAgent:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.client = None
        if self.api_key:
            self.client = AsyncOpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com"
            )

    async def execute(self, prompt: str) -> str:
        if not self.client:
            return "Error: DEEPSEEK_API_KEY not found in environment variables."

        try:
            response = await self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"Employee DeepSeek is currently unreachable. Please try again in a moment. Error: {str(e)}"

import os
from anthropic import AsyncAnthropic

class ClaudeAgent:
    def __init__(self):
        self.api_key = os.getenv("CLAUDE_API_KEY")
        self.client = None
        if self.api_key:
            self.client = AsyncAnthropic(api_key=self.api_key)

    async def execute(self, prompt: str) -> str:
        if not self.client:
            return "Error: CLAUDE_API_KEY not found in environment variables."

        try:
            message = await self.client.messages.create(
                model="claude-3-5-sonnet-latest",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Extract text from the first content block
            if message.content and len(message.content) > 0:
                return message.content[0].text
            return "Error: Empty response from Claude."

        except Exception as e:
            return f"Employee Claude is currently unreachable. Please try again in a moment. Error: {str(e)}"

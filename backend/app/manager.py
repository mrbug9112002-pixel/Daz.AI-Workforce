from app.models import TaskResponse
from app.agents.gemini import GeminiAgent
from app.agents.claude import ClaudeAgent
from app.agents.deepseek import DeepSeekAgent

class ManagerAgent:
    def __init__(self):
        self.gemini = GeminiAgent()
        self.claude = ClaudeAgent()
        self.deepseek = DeepSeekAgent()

    async def process_task(self, prompt: str) -> TaskResponse:
        """
        Analyzes the prompt and routes it to the appropriate agent using a Weighted Scoring System.
        """
        prompt_lower = prompt.lower()
        
        # Define keywords and their weights for each agent
        # Higher weight = stronger indicator
        agent_scores = {
            "claude": {"score": 0, "name": "Claude (Coding Expert)", "keywords": {
                "code": 10, "python": 10, "javascript": 10, "react": 10, "css": 10, "sql": 10,
                "function": 5, "debug": 8, "api": 5, "error": 5, "fix": 5, "app": 3
            }},
            "deepseek": {"score": 0, "name": "DeepSeek (Reasoning Expert)", "keywords": {
                "analyze": 5, "analysis": 5, "logic": 8, "reasoning": 8, "complex": 5, 
                "math": 10, "strategy": 5, "compare": 5, "difference": 5, "why": 3, "how": 3
            }},
            "gemini": {"score": 0, "name": "Gemini (Creative Expert)", "keywords": {
                "story": 10, "poem": 10, "creative": 10, "write": 5, "email": 5, 
                "blog": 8, "idea": 5, "marketing": 5, "design": 3, "generate": 3
            }}
        }

        # Calculate scores
        for agent_key, data in agent_scores.items():
            for word, weight in data["keywords"].items():
                if word in prompt_lower:
                    data["score"] += weight

        # Determine winner
        # Sort by score descending
        sorted_agents = sorted(agent_scores.values(), key=lambda x: x["score"], reverse=True)
        winner = sorted_agents[0]
        
        # Edge Case: If no keywords match (score 0), use General Assistant (Gemini)
        # Or if there is a conflict, the weights help deciding.
        # e.g. "Analysis of Python Code":
        # - Claude: "python"(10) + "code"(10) = 20
        # - DeepSeek: "analysis"(5) = 5
        # -> Winner: Claude (Correct, as it requires coding knowledge)
        
        if winner["score"] == 0:
             # Default fallback
            agent_name = "Gemini (General Assistant)"
            result = await self.gemini.execute(prompt)
        else:
            agent_name = winner["name"]
            if "Claude" in agent_name:
                result = await self.claude.execute(prompt)
            elif "DeepSeek" in agent_name:
                result = await self.deepseek.execute(prompt)
            else:
                result = await self.gemini.execute(prompt)

        return TaskResponse(
            assigned_agent=agent_name,
            result=result,
            status="success"
        )

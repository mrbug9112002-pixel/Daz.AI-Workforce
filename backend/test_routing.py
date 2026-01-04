import asyncio
from app.manager import ManagerAgent

async def test_routing():
    manager = ManagerAgent()
    
    test_cases = [
        ("Write a python function to sort a list", "Claude"),
        ("I need an analysis of my Python code's logic", "Claude"),
        ("Write a creative story about a robot", "Gemini"),
        ("Analyze the complex logic of this math problem", "DeepSeek"),
        ("Debug this React component", "Claude"),
        ("What is the meaning of life?", "Gemini"), # Fallback
    ]
    
    print(f"{'Prompt':<50} | {'Expected':<10} | {'Actual':<30} | {'Result'}")
    print("-" * 110)
    
    for prompt, expected in test_cases:
        response = await manager.process_task(prompt)
        actual = response.assigned_agent
        # Check if expected name acts as a substring in actual (e.g. "Claude" in "Claude (Coding Expert)")
        success = expected in actual
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{prompt[:47]+'...':<50} | {expected:<10} | {actual:<30} | {status}")

if __name__ == "__main__":
    asyncio.run(test_routing())

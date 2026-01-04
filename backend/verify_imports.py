import os
import sys

# Mock env vars for testing instantiation
os.environ["GEMINI_API_KEY"] = "fake_key"
os.environ["CLAUDE_API_KEY"] = "fake_key"
os.environ["DEEPSEEK_API_KEY"] = "fake_key"

try:
    print("Testing imports...")
    from app.agents.gemini import GeminiAgent
    from app.agents.claude import ClaudeAgent
    from app.agents.deepseek import DeepSeekAgent
    from app.manager import ManagerAgent
    print("Imports successful.")

    print("Testing instantiation...")
    gemini = GeminiAgent()
    claude = ClaudeAgent()
    deepseek = DeepSeekAgent()
    manager = ManagerAgent()
    print("Instantiation successful.")
    print("✅ Syntax Verification Passed")

except Exception as e:
    print(f"❌ Verification Failed: {e}")
    sys.exit(1)

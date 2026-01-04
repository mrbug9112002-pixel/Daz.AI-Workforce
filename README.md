# Daz.AI-Workforce

**"Your AI Workforce, Managed."**

Welcome to Daz.AI-Workforce. This platform allows you to delegate tasks to a team of specialized AI agents. You simply type what you need, and our intelligent **Manager Agent** decides which expert AI (Gemini, Claude, or DeepSeek) is best suited to handle it.

## 🚀 How It Works
1.  **You** enter a task in the clean, modern dashboard.
2.  The **Manager Agent** (Backend) analyzes your request.
    - *Need code?* It calls **Claude**.
    - *Need creative writing?* It calls **Gemini**.
    - *Need complex reasoning?* It calls **DeepSeek**.
3.  The result is displayed instantly on your screen.

## 🛠 Project Structure
This project is divided into two main parts:
- **Frontend (The Dashboard)**: Built with Next.js & Tailwind CSS. This is what you see.
- **Backend (The Brain)**: Built with Python & FastAPI. This is where the decisions happen.

## 🚦 Getting Started (Simple Version)

### Prerequisites
You need to have these installed on your computer:
1.  **Python** (for the backend logic)
2.  **Node.js** (for the frontend dashboard)

### Setup Instructions

#### 1. Setup the Backend (The Brain)
Open your terminal/command prompt and run:

```bash
cd backend
pip install -r requirements.txt
# Create a .env file with your API keys (Instructions will be provided in Phase 2)
# python -m uvicorn main:app --reload
```

#### 2. Setup the Frontend (The Dashboard)
Open a *new* terminal window and run:

```bash
cd frontend
npm install
# npm run dev
```

Then open your browser to `http://localhost:3000`.

---
*Created by Antigravity*

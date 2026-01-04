from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.manager import ManagerAgent
from app.models import TaskRequest, TaskResponse
import os
from typing import Optional

# Load environment variables
load_dotenv()

app = FastAPI(title="Daz.AI-Workforce Backend")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ManagerAgent()
ACCESS_CODE = os.getenv("APP_ACCESS_CODE")

async def verify_access_code(x_access_code: Optional[str] = Header(None)):
    if not ACCESS_CODE:
        # If no code is set in env, allow open access (or default to secure, let's allow open for dev convenience unless set)
        return
    if x_access_code != ACCESS_CODE:
        raise HTTPException(status_code=401, detail="Invalid Access Code")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Daz.AI-Workforce Brain is running"}

@app.post("/execute", response_model=TaskResponse)
async def execute_task(request: TaskRequest, authorized: bool = Depends(verify_access_code)):
    """
    Endpoint to receive a user task, determine the best agent, and execute it.
    Secured by Access Code.
    """
    result = await manager.process_task(request.prompt)
    return result

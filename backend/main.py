import asyncio
import cognee
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ThreatDNA API")

class RememberRequest(BaseModel):
    content: str

class RecallRequest(BaseModel):
    query: str

class ForgetRequest(BaseModel):
    dataset_name: str

@app.post("/remember")
async def remember_incident(request: RememberRequest):
    await cognee.remember(request.content)
    return {"status": "stored", "message": "Incident added to ThreatDNA memory"}

@app.post("/recall")
async def recall_incident(request: RecallRequest):
    results = await cognee.recall(request.query)
    return {"query": request.query, "results": [str(r) for r in results]}

@app.post("/improve")
async def improve_memory():
    await cognee.improve()
    return {"status": "improved", "message": "Memory relationships strengthened"}

@app.post("/forget")
async def forget_data(request: ForgetRequest):
    await cognee.forget(dataset_name=request.dataset_name)
    return {"status": "forgotten", "dataset": request.dataset_name}

@app.get("/")
async def root():
    return {"message": "ThreatDNA API is running"}
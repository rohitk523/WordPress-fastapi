from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your WordPress domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data models
class ServiceEvent(BaseModel):
    title: str
    date: str
    description: Optional[str] = None

# Sample data
events = [
    {"title": "Sunday Service", "date": "2024-12-01", "description": "Morning Worship"},
    {"title": "Prayer Meeting", "date": "2024-12-03", "description": "Evening Prayer"}
]

@app.get("/")
def read_root():
    return {"message": "Church Tools API is running!"}

@app.get("/events")
def get_events():
    return {"events": events}

@app.get("/service/{service_id}")
def get_service(service_id: int):
    if service_id < len(events):
        return events[service_id]
    return {"error": "Service not found"}

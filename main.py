from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/church-page", response_class=HTMLResponse)
async def get_church_page(request: Request):
    return templates.TemplateResponse("church_page.html", {"request": request})

@app.get("/events")
async def get_events():
    events = [
        {"title": "Sunday Service", "date": "2024-12-01"},
        {"title": "Prayer Meeting", "date": "2024-12-03"},
        {"title": "Youth Group", "date": "2024-12-04"},
        {"title": "Bible Study", "date": "2024-12-05"}
    ]
    return {"events": events}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
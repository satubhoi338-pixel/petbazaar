from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")
generator = pipeline("text-generation", model="gpt2")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
def chat(request: Request, prompt: str = Form(...)):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return templates.TemplateResponse("index.html", {"request": request, "response": result[0]["generated_text"]})

from fastapi import FastAPI
from pydantic import BaseModel
from ai_utils import transform_text   # import your function

app = FastAPI(title="Alternate Universe Rewriter")

class ChatRequest(BaseModel):
    text: str
    universe: str

@app.post("/chat/")
def chat(request: ChatRequest):
    text = request.text
    universe = request.universe.lower()
    
    # Call AI function instead of placeholder
    transformed_text = transform_text(text, universe)

    return {
        "original": text,
        "universe": universe,
        "response": transformed_text
    }

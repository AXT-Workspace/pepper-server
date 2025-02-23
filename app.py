from fastapi import FastAPI
from models.chat import Chat, ChatResponse
from models.root import RootResponse
from models.i_dont_care import IDontCareResponse
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
app = FastAPI()

client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))

@app.get("/")
async def root() -> RootResponse:
  return RootResponse(message="Hello World")

@app.get("/I/don't/care")
async def i_dont_care() -> IDontCareResponse:
  return IDontCareResponse(message="I don't care", mood="happy")

@app.post("/chat")
async def chat(chat: Chat) -> ChatResponse:
  # client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
  response = client.models.generate_content(
    model="gemini-2.0-flash-lite-preview-02-05", contents=chat.message
  )
  print(response.text)
  return ChatResponse(response=response.text, mood="happy")

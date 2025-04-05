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
PORT = int(os.getenv("PORT", 8000))

@app.get("/", summary="Root endpoint", description="This endpoint checks if the server is running.")
async def root() -> RootResponse:
  return RootResponse(message="Hello World")

@app.get("/I/don't/care", summary="I don't care", description="Fun pivot during development.")
async def i_dont_care() -> IDontCareResponse:
  return IDontCareResponse(message="I don't care", mood="happy")

@app.post("/chat/simple", summary="Chat with the AI", description="This endpoint sends a chat message to the AI model and returns the response.")
async def chat(chat: Chat) -> ChatResponse:
  client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
  response = client.models.generate_content(
    model="gemini-2.0-flash-lite-preview-02-05", contents=chat.message
  )
  print(response.text)
  return ChatResponse(response=response.text, mood="happy")

@app.post("/chat/standard", summary="", description="This endpoint sends a chat message to the AI model and returns the response.")
async def chat(chat: Chat) -> ChatResponse:
  client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
  response = client.models.generate_content(
    model="gemini-2.0-flash-lite-preview-02-05", contents=chat.message
  )
  print(response.text)
  return ChatResponse(response=response.text, mood="happy")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=True, log_level="info")
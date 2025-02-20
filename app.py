from fastapi import FastAPI

from models.chat import Chat

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/I/don't/care")
async def i_dont_care():
  return {"message": "I don't care", "mood": "happy"}

@app.post("/chat")
async def chat(chat: Chat):
  print(chat)

  return {"response": "Loud and clear", "mood": "happy"}
from pydantic import BaseModel

class Chat(BaseModel):
  message: str
  mood: str
  personId: str

class ChatResponse(BaseModel):
  response: str
  mood: str
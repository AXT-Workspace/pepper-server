from pydantic import BaseModel

class Chat(BaseModel):
  message: str
  mood: str
  personId: str
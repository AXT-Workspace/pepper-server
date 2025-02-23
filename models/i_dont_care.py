from pydantic import BaseModel

class IDontCareResponse(BaseModel):
  message: str
  mood: str
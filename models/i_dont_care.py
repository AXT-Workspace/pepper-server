from pydantic import BaseModel, Field

class IDontCareResponse(BaseModel):
  message: str = Field(description="String containing 'I don't care' in it.")
  mood: str = Field(description="String containing 'happy' in it.")
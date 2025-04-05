from pydantic import BaseModel, Field

class Chat(BaseModel):
  message: str = Field(description="The message to send to the AI model.")
  # mood: str = Field(description="The mood of the message.")
  # personId: str = Field(description="The ID of the person sending the message.")

class ChatResponse(BaseModel):
  response: str = Field(description="The response from the AI model.")
  mood: str = Field(description="The mood of the response.")
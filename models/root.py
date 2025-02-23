from pydantic import BaseModel, Field

class RootResponse(BaseModel):
  message: str = Field(description="The response to confirm that the server is running.")
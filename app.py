from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/I/don't/care")
async def i_dont_care():
  return {"message": "I don't care", "mood": "happy"}
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return{"message":"Hello ji FASTAPI kaam kr rha hai"}
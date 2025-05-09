from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_root():
    print("Root endpoint called")
    return {"message": "Hello World"}

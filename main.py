from fastapi import FastAPI

app = FastAPI() # for now am not going to pass any parameter to the Fastapi class 



@app.get("/")
async def root():
    return {"messange":"hello world"}


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "backend is up and running"
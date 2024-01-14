from fastapi import FastAPI

#from backend.api import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
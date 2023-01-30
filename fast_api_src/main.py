import os

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/info")
async def info():
    return {"python host": os.getenv("PYHOST"), "instance id": os.getenv("INSTANCE_ID")}

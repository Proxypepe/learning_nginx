from fastapi import FastAPI
import uuid

app = FastAPI()
uuid_gen = str(uuid.uuid4())

@app.get("/")
def read_root():
    return {"uuid": uuid_gen}

@app.get("/uuid")
def read_uuid():
    return {"uuid": uuid_gen}

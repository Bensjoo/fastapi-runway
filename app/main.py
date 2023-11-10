
from fastapi import FastAPI
from app.config import Config


# get the config file
conf = Config()

# fastAPI Instance
app = FastAPI(title="FastAPI Template")


@app.get('/')
async def root():
    return {"message": "FastAPI template"}


@app.get('/readyz')
async def readyz():
    return {"message": 200}

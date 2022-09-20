from fastapi import FastAPI

from schemas.api_request import APIRequest
from schemas.api_response import APIResponse

app = FastAPI()


@app.get("/health")
def health_check():
    return {"health check": "ok"}


@app.get("/law/21_1")
def law_21_1(body: APIRequest):


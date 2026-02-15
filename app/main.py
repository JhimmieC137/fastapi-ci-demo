from fastapi import FastAPI
from app.models import BaseParams


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.post("/sum")
def calc_sum(sum_params: BaseParams):
    abs_left = sum_params.left if sum_params else 0
    abs_right = sum_params.right if sum_params else 0
    sum = abs_left + abs_right

    return {
        "status": 200,
        "message": "successful",
        "result": sum
    }

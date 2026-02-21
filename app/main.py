from fastapi import FastAPI
from app.models import BaseParams, DivideParams


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


@app.post("/sub")
def calc_sub(sum_params: BaseParams):
    abs_left = sum_params.left if sum_params else 0
    abs_right = sum_params.right if sum_params else 0
    sub = abs_left - abs_right

    return {
        "status": 200,
        "message": "successful",
        "result": sub
    }


@app.post("/multiply")
def calc_multiply(sum_params: BaseParams):
    abs_left = sum_params.left if sum_params else 0
    abs_right = sum_params.right if sum_params else 0
    mult = abs_left * abs_right

    return {
        "status": 200,
        "message": "successful",
        "result": mult
    }


@app.post("/divide")
def calc_divide(sum_params: DivideParams):
    abs_left = sum_params.left if sum_params else 0
    abs_right = sum_params.right if sum_params else 0
    divided = abs_left / abs_right

    return {
        "status": 200,
        "message": "successful",
        "result": divided
    }

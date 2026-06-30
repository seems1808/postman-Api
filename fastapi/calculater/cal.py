from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Calculator"}

@app.get("/add")
def add(a: float, b: float):
    return {
        "operation": "Addition",
        "num1": a,
        "num2": b,
        "result": a + b
    }

@app.get("/subtract")
def subtract(a: float, b: float):
    return {
        "operation": "Subtraction",
        "num1": a,
        "num2": b,
        "result": a - b
    }

@app.get("/multiply")
def multiply(a: float, b: float):
    return {
        "operation": "Multiplication",
        "num1": a,
        "num2": b,
        "result": a * b
    }

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}

    return {
        "operation": "Division",
        "num1": a,
        "num2": b,
        "result": a / b
    }

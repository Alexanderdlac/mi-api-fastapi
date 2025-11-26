from fastapi import FastAPI

app = FastAPI()

W = 2
b = 0

@app.get("/predict")
def predict(x: float):
    return {"prediction": W * x + b}

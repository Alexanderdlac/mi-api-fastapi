from fastapi import FastAPI, Request

app = FastAPI()

# --- Tu modelo (simple W y b) ---
W = 2
b = 0

# --- Middleware para ver las peticiones en los Logs de Render ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"📥 {request.method} {request.url}")    # Log de entrada
    response = await call_next(request)
    print(f"📤 Status: {response.status_code}")   # Log de salida
    return response

# --- Endpoint ---
@app.get("/predict")
def predict(x: float):
    return {"prediction": W * x + b}

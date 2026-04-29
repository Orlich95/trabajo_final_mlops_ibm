from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_close


app = FastAPI(title="IBM Stock Price Prediction API")


class StockInput(BaseModel):
    open_price: float
    high: float
    low: float
    volume: float


@app.get("/")
def home():
    return {"message": "IBM Stock Price Prediction API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: StockInput):
    prediction = predict_close(
        open_price=data.open_price,
        high=data.high,
        low=data.low,
        volume=data.volume,
    )

    return {
        "predicted_close": prediction
    }
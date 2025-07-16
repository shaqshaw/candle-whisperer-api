from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database import load_trades, save_trade, load_predictions, save_prediction
from datetime import datetime

app = FastAPI()

class PredictInput(BaseModel):
    input_data: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Candle Whisperer API!"}

@app.post("/predict")
def predict_webhook(payload: PredictInput):
    prediction = {
        "id": int(datetime.utcnow().timestamp()),
        "input": payload.dict(),
        "trend": "up",
        "confidence": 0.87,
        "created_at": datetime.utcnow().isoformat() + 'Z'
    }
    save_prediction(prediction)
    return JSONResponse({
        "status": "success",
        "input": prediction["input"],
        "prediction": {
            "trend": prediction["trend"],
            "confidence": prediction["confidence"]
        },
        "id": prediction["id"],
        "created_at": prediction["created_at"]
    })

@app.get("/trade")
def get_trade():
    trade = {
        "trade_id": int(datetime.utcnow().timestamp()),
        "symbol": "BTCUSD",
        "action": "buy",
        "amount": 0.5,
        "price": 65000.0,
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }
    save_trade(trade)
    return trade 
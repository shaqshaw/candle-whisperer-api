from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database import load_trades, load_predictions
from datetime import datetime
import asyncio

app = FastAPI()

class PredictInput(BaseModel):
    input_data: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Candle Whisperer API!"}

@app.websocket("/predict")
async def predict_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            predictions = load_predictions()
            latest = predictions[-1] if predictions else {}
            await websocket.send_json(latest)
            await asyncio.sleep(1)
    except Exception:
        await websocket.close()

@app.get("/trade")
def get_trade():
    # Hardcoded mock trade data
    trade = {
        "trade_id": 123456,
        "symbol": "BTCUSD",
        "action": "buy",
        "amount": 0.5,
        "price": 65000.0,
        "timestamp": "2024-07-01T12:00:00Z"
    }
    return trade 
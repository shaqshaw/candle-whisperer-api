import json
import os

MOCK_TRADES_FILE = os.path.join(os.path.dirname(__file__), 'mock_trades.json')
MOCK_PREDICTIONS_FILE = os.path.join(os.path.dirname(__file__), 'mock_predictions.json')

def load_trades():
    if not os.path.exists(MOCK_TRADES_FILE):
        return []
    with open(MOCK_TRADES_FILE, 'r') as f:
        return json.load(f)

def save_trade(trade):
    trades = load_trades()
    trades.append(trade)
    with open(MOCK_TRADES_FILE, 'w') as f:
        json.dump(trades, f, indent=2)

def load_predictions():
    if not os.path.exists(MOCK_PREDICTIONS_FILE):
        return []
    with open(MOCK_PREDICTIONS_FILE, 'r') as f:
        return json.load(f)

def save_prediction(prediction):
    predictions = load_predictions()
    predictions.append(prediction)
    with open(MOCK_PREDICTIONS_FILE, 'w') as f:
        json.dump(predictions, f, indent=2) 
from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.pkl"


def predict_close(open_price, high, low, volume):
    model = joblib.load(MODEL_PATH)

    input_data = pd.DataFrame(
        [
            {
                "Open": open_price,
                "High": high,
                "Low": low,
                "Volume": volume,
            }
        ]
    )

    prediction = model.predict(input_data)

    return float(prediction[0])
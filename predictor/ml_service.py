from functools import lru_cache
from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml_models" / "random_forest_expense_categorisation_pipeline.joblib"

@lru_cache(maxsize=1)
def load_model():
    return joblib.load(MODEL_PATH)

def build_model_input(cleaned):
    d = cleaned["transaction_date"]
    return pd.DataFrame([{
        "Description": cleaned["description"],
        "Amount": float(cleaned["amount"]),
        "PaymentMethod": cleaned["payment_method"],
        "Location": cleaned["location"],
        "AccountType": cleaned["account_type"],
        "DeviceUsed": cleaned["device_used"],
        "MerchantType": cleaned["merchant_type"],
        "LoyaltyProgram": 1 if cleaned["loyalty_program"] == "Yes" else 0,
        "TimeOfDay": cleaned["time_of_day"],
        "Month": d.month,
        "DayOfWeek": d.weekday(),
    }])

def predict_expense(cleaned):
    model = load_model()
    row = build_model_input(cleaned)
    prediction = str(model.predict(row)[0])
    return prediction, row.iloc[0].to_dict()

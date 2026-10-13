from pathlib import Path
import joblib, pandas as pd
BASE = Path(__file__).resolve().parent
model = joblib.load(BASE/"ml_models"/"random_forest_expense_categorisation_pipeline.joblib")
df = pd.read_csv(BASE/"data"/"personal_finance_dataset_8000_extended.csv")
r = df.iloc[0]
date = pd.to_datetime(r["Date"], format="%m/%d/%Y")
x = pd.DataFrame([{
    "Description": r["Description"], "Amount": float(r["Amount"]),
    "PaymentMethod": r["PaymentMethod"], "Location": r["Location"],
    "AccountType": r["AccountType"], "DeviceUsed": r["DeviceUsed"],
    "MerchantType": r["MerchantType"], "LoyaltyProgram": 1 if r["LoyaltyProgram"]=="Yes" else 0,
    "TimeOfDay": r["TimeOfDay"], "Month": date.month, "DayOfWeek": date.dayofweek
}])
print("Dataset actual category:", r["Category"])
print("Random Forest prediction:", model.predict(x)[0])
print("Random Forest model loaded and prediction test completed.")

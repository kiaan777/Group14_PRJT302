from django import forms
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET = BASE_DIR / "data" / "personal_finance_dataset_8000_extended.csv"

def choices(column):
    df = pd.read_csv(DATASET, usecols=[column])
    values = sorted(df[column].dropna().astype(str).unique())
    return [("", "Select an option")] + [(v, v) for v in values]

class ExpenseForm(forms.Form):
    description = forms.ChoiceField(label="Description", choices=choices("Description"))
    amount = forms.DecimalField(label="Amount", min_value=0.01, max_digits=12, decimal_places=2,
                                widget=forms.NumberInput(attrs={"step":"0.01", "placeholder":"e.g. 450.00"}))
    payment_method = forms.ChoiceField(label="Payment Method", choices=choices("PaymentMethod"))
    location = forms.ChoiceField(label="Location", choices=choices("Location"))
    account_type = forms.ChoiceField(label="Account Type", choices=choices("AccountType"))
    device_used = forms.ChoiceField(label="Device Used", choices=choices("DeviceUsed"))
    merchant_type = forms.ChoiceField(label="Merchant Type", choices=choices("MerchantType"))
    loyalty_program = forms.ChoiceField(label="Loyalty Program", choices=[("", "Select an option"), ("No","No"), ("Yes","Yes")])
    time_of_day = forms.ChoiceField(label="Time of Day", choices=choices("TimeOfDay"))
    transaction_date = forms.DateField(label="Transaction Date", widget=forms.DateInput(attrs={"type":"date"}))

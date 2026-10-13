from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import PredictionHistory
from .ml_service import predict_expense, load_model

MODEL_METRICS = {
    "accuracy": "99.63%",
    "f1": "99.62%",
    "training_time": "0.30 s",
}

COMPARISON = {
    "svm_accuracy": "98.56%",
    "svm_f1": "98.53%",
    "rf_accuracy": "99.63%",
    "rf_f1": "99.62%",
}

def dashboard(request):
    result = None
    form = ExpenseForm(request.POST or None)
    model_loaded = False
    try:
        load_model()
        model_loaded = True
    except Exception:
        pass

    if request.method == "POST" and form.is_valid():
        prediction, model_input = predict_expense(form.cleaned_data)
        PredictionHistory.objects.create(
            description=form.cleaned_data["description"],
            amount=form.cleaned_data["amount"],
            payment_method=form.cleaned_data["payment_method"],
            location=form.cleaned_data["location"],
            account_type=form.cleaned_data["account_type"],
            device_used=form.cleaned_data["device_used"],
            merchant_type=form.cleaned_data["merchant_type"],
            loyalty_program=form.cleaned_data["loyalty_program"],
            time_of_day=form.cleaned_data["time_of_day"],
            transaction_date=form.cleaned_data["transaction_date"],
            predicted_category=prediction,
        )
        result = {
            "prediction": prediction,
            "month": model_input["Month"],
            "day_of_week": model_input["DayOfWeek"],
        }

    return render(request, "predictor/index.html", {
        "form": form,
        "result": result,
        "history": PredictionHistory.objects.all()[:8],
        "metrics": MODEL_METRICS,
        "comparison": COMPARISON,
        "model_loaded": model_loaded,
    })

def clear_history(request):
    if request.method == "POST":
        PredictionHistory.objects.all().delete()
    return redirect("dashboard")

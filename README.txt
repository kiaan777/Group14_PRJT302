PRJT302 - RANDOM FOREST DJANGO EXPENSE CATEGORISATION
======================================================

PURPOSE
The Jupyter experiment trained and evaluated SVM and Random Forest using the same
80/20 split. Random Forest recorded the stronger measured classification results
in that experiment and is therefore the only model deployed in this prototype.

DEPLOYED MODEL
Random Forest
Recorded test Accuracy: 99.63%
Recorded Macro F1: 99.62%
Training records: 6,400
Testing records: 1,600

WHAT THE APP DOES
- No login: opens directly to the categorisation dashboard.
- Loads only random_forest_expense_categorisation_pipeline.joblib.
- Uses real dataset values for categorical dropdowns.
- Uses a dataset-backed Description dropdown for reproducible demonstrations.
- Accepts Amount and Transaction Date.
- Derives Month and DayOfWeek automatically.
- Calls the fitted Random Forest pipeline's .predict() method.
- Displays the live predicted expense category.
- Stores recent predictions in local SQLite history.
- Shows model-selection evidence from the SVM vs Random Forest experiment.

QUICK WINDOWS START
1. Extract the ZIP.
2. Open the extracted folder.
3. Double-click START_APP.bat.
4. The app opens at http://127.0.0.1:8000/

VS CODE
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

MODEL FILE
ml_models/random_forest_expense_categorisation_pipeline.joblib

The prediction is not hard-coded. Django loads the fitted model and calls .predict()
for each submitted transaction.

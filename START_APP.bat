@echo off
title PRJT302 Expense Categorisation
echo.
echo PRJT302 Expense Categorisation
echo ==============================
if not exist .venv (
  echo Creating virtual environment...
  python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
echo.
echo Opening app at http://127.0.0.1:8000/
start "" http://127.0.0.1:8000/
python manage.py runserver
pause

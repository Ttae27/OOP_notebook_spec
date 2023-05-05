@echo off
echo Start backend

REM Run uvicorn on main.py
start "Backend" /B uvicorn main:app --reload

REM Pause briefly
timeout /t 2 /nobreak > NUL

echo Start frontend
REM Run ./front/home_ui.py
python %CD%\front\home_ui.py

echo Finished
pause

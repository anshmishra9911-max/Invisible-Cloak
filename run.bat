@echo off
echo Installing requirements...
pip install -r requirements.txt
echo.
echo First, let's capture background...
python background.py
echo.
echo Now running invisibility cloak...
python invisible_cloak.py
pause
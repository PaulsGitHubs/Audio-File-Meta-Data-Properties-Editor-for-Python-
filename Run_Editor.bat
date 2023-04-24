@echo off

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/ and try again.
    pause
    exit /B 1
)

echo Running Metadata_Editor.py...
python Metadata_Editor.py
pause

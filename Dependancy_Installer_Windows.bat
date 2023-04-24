@echo off

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/ and try again.
    pause
    exit /B 1
)

where pip >nul 2>&1
if errorlevel 1 (
    echo Installing pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

echo Installing PyQt5...
pip install PyQt5

echo Installing taglib-python...
pip install taglib-python

echo All dependencies have been installed. You can now run the Python script.
pause

@echo off
echo Iniciando Sistema de Soporte TI Basico...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Usando Python...
    python main.py
) else (
    python3 --version >nul 2>&1
    if %errorlevel% == 0 (
        echo Usando Python3...
        python3 main.py
    ) else (
        echo ERROR: Python no está instalado o no está en el PATH
        echo.
        echo Por favor, instale Python desde https://python.org
        echo o asegúrese de que Python esté en el PATH del sistema
        echo.
        pause
    )
)

pause

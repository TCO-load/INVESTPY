@echo off
echo Installation des dependances et lancement du conseiller d'investissement DCA...

REM Verifier si Python est installe
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python et l'ajouter au PATH.
    pause
    exit /b 1
)

REM Installer ou mettre a jour pip
python -m ensurepip --upgrade

REM Installer les dependances
pip install colorama matplotlib pandas seaborn

REM Lancer le programme
python invest.py

pause
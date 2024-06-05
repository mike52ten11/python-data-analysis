@echo off
echo.
echo. 一鍵安裝 Aanconda Python 環境

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

cd C:\code\python-data-analysis
call conda activate python_data_analysis
call conda env list
spyder
call conda deactivate
pause
@echo on
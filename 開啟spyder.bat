@echo off
echo.
echo. �@��w�� Aanconda Python ����

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

cd C:\code\python-data-analysis
call conda activate python_data_analysis
call conda env list
spyder
call conda deactivate
pause
@echo on
@echo off
echo.
echo. �@��w�� Aanconda Python ����

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

cd C:\code\awstpri
call conda activate python_lesson
call conda env list
jupyter notebook
call conda deactivate
pause
@echo on
@echo off
echo.
echo. 一鍵安裝 Aanconda Python 環境

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

cd C:\code\awstpri
call conda activate python_lesson
call conda env list
jupyter notebook
call conda deactivate
pause
@echo on
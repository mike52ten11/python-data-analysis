@echo off
echo.
echo. 一鍵安裝 Aanconda Python 環境



curl -x http://proxy-n1.taipower.com.tw:3128 https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

mkdir C:\code
cd C:\code
git config --global https.proxy http://proxy-n1.taipower.com.tw:3128
git config --global http.proxy http://proxy-n1.taipower.com.tw:3128 
git clone https://github.com/mike52ten11/awstpri.git
cd C:\code\awstpri

echo Y | call conda create -n python_lesson python==3.9

cd C:\code\awstpri
call conda activate python_lesson
call conda env list
call C:\ProgramData\miniconda3\envs\python_lesson\Scripts\pip.exe install --proxy http://proxy-n1.taipower.com.tw:3128 -r requirements.txt
if NOT ["%errorlevel%"]==["0"] (  python -m pip install --proxy http://proxy-n1.taipower.com.tw:3128 --upgrade setuptools )
call C:\ProgramData\miniconda3\envs\python_lesson\Scripts\pip.exe install --proxy http://proxy-n1.taipower.com.tw:3128 -r requirements.txt
jupyter notebook
call conda deactivate
pause
@echo on
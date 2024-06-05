@echo off
echo.
echo. 一鍵安裝 Aanconda Python 環境

curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe

CALL C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3
mkdir C:\code
cd C:\code
git clone https://github.com/mike52ten11/python-data-analysis.git
cd python-data-analysis


call conda create -n python_data_analysis python==3.9
call conda activate python_data_analysis
call C:\ProgramData\miniconda3\envs\python_data_analysis\Scripts\pip.exe install -r requirements.txt
if NOT ["%errorlevel%"]==["0"] (  python -m pip install  --upgrade setuptools )
call C:\ProgramData\miniconda3\envs\python_data_analysis\Scripts\pip.exe install -r requirements.txt
spyder
call conda deactivate
pause
@echo on
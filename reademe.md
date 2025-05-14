#  stopping all Python processes 
taskkill /F /IM python.exe

uvicorn bookapi.books:app --reload --reload-dir=./bookapi



# TO CREATE THE ENVIRONMNET
python -m venv fastapienv
# TO ACTIVATE THE ENVIRONMNET 
fastapienv\Scripts\activate.bat 

# TO LSIT PIP LSIT
pip list

# TO DOWNLAOD FASTAPI AND UVICORN(webserver for fastapi)
pip install fastapi
pip install "uvicorn"

# TO DEACTIVATE 
deactivate


# TO RUN API ENDPOINTS
uvicorn [fileName]:app --reload
uvicorn books:app --reload 
or
# TO THIS COMMAND WORK YOU NEED TO INSTALL THIS PAKAGE
pip install "fastapi[standard]"

pip show uvicorn


# THEN RUN 
fastapi run/dev [fileName].py
fastapi run books.py 

# The easiest way to install pyenv-win is to run the following installation command in a PowerShell terminal:
# This will download the installation script and execute it. The script will install pyenv-win to the default location, which is C:\Users\{User}\.pyenv.
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"


# CLOse the PowerShell terminal and open a new one to ensure that the changes take effect. You can verify that pyenv-win is installed by running the following command:
pyenv --version

# TO CHECK THE PYTHON VERSION
pyenv exec python -V

# TO CREATE A VIRTUAL ENVIRONMENT
pyenv exec python -m venv .venv
# TO ACTIVATE THE VIRTUAL ENVIRONMENT   
.\.venv\Scripts\activate
# TO INSTALL THE DEPENDENCIES   
pip install -r requirements.txt
# TO DEACTIVATE THE VIRTUAL ENVIRONMENT 
deactivate

# TO INSTALL THE DEPENDENCIES from the requirements.txt file
pip install -r .\requirements.txt


uvicorn bookapu.book:app --reload
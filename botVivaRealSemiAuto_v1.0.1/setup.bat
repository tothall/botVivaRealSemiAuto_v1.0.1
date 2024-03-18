echo instalando...
py -3.9 -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pip freeze
pause
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


Task 00:

python3 credentials.py
curl http://127.0.0.1:8888/?species=Time%20Lord


Task 01:

python3 manage.py runserver 8888

http://localhost:8888/UploadFile

python3 screwdriver.py list

python3 screwdriver.py upload some_file.mp3

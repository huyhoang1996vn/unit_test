virtualenv -p python3.8 venv

source venv/bin/activate

pip install -r requiments.txt

export FLASK_APP=flask_api

flask run

pytest test.py

https://circleci.com/blog/testing-flask-framework-with-pytest/
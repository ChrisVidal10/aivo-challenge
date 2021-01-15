#!bin/bash

flask db init
flask db migrate
flask db upgrade
python3 load_script.py
flask run
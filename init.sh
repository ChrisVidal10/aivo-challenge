#!bin/bash

flask db init
flask db migrate
flask db upgrade
python3 scripts/load_script.py
flask run
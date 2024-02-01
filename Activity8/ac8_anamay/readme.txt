Create By Anamay Dubey

create a virtual env 

virtualenv env

pip install flask
pip install flask-sqlalchemy

Run the app.py

if you face any error related to database

- Delete db file from Instance folder

-In shell write these commands

from app import app
from app import db
app.app_context().push()
db.create_all()
exit()

run app.py again 

This project was created for activity 8 . Thank You!
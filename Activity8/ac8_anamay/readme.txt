Create By Anamay Dubey

1.create a virtual env ,In shell type -
-virtualenv env
-./env/Scripts/activate
-pip install flask
-pip install flask-sqlalchemy

2.Run the app.py
3.Click on link you see in the terminal

4.If you face any error related to database

- Delete db file from Instance folder

-In shell write these commands

from app import app
from app import db
app.app_context().push()
db.create_all()
exit()

run app.py again 

This project was created for activity 8 . Thank You!

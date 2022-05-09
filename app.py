# pip install sqlalchemy-bigquery
# pip install dash
# pip install sqlalchemy
# pip install flask_sqlalchemy

import dash
import os

from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.engine import create_engine
from flask_sqlalchemy import SQLAlchemy


app = dash.Dash(__name__,  update_title='Atualizando...')
server = app.server
app.config.suppress_callback_exceptions = True

db = SQLAlchemy()
 
# BIGQUERY
project_id = ''
dataset_name = ''
credentials = 'path to .json'
url = 'bigquery://'+project_id+"/"+dataset_name+"?credentials_path="+credentials

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=url, 
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)

engine = create_engine('bigquery://project id/dataset name', credentials_path='path to .json')
userTable = Table('table name', MetaData(bind=engine), autoload=True)
userTable = Table('user', User.metadata)

# Do your user managment...

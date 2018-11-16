from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pickle
# Creates the application object 
app = Flask(__name__,static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IIITHSO.db'
db = SQLAlchemy(app)

index_qid = 0
index_ans_id = 0
with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([index_ans_id, index_qid], f)

from app import views



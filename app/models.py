from app import db
from datetime import date
import datetime
import calendar
from sqlalchemy import ForeignKey, types
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence, MetaData
from sqlalchemy import PrimaryKeyConstraint


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    #id = db.Column(db.Integer, primary_key=True)
    month_name = calendar.month_name[date.today().month]
    year = date.today().year
    since = month_name + " "+ str(year)
    username = db.Column(db.String(20), unique=True, nullable=False,primary_key = True)
    password = db.Column( db.String(60), nullable=False)
    display_name = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(60), nullable = False)
    reputation = db.Column( db.Integer, default = 0)
    joined = db.Column(db.String, default = since)
    profile_image = db.Column(db.String(30), nullable=True)
    profile_image_data = db.Column(db.LargeBinary)
    user_bio = db.Column(db.Text, nullable = True)
    asks_ques = db.relationship('Questions', lazy=True)
    answers_ques = db.relationship('Answers', lazy = True)
    

    def __repr__(self):
        return "User('{self.username}, {self.password}, {self.email}, {Self.reputation}, {self.joined}')"

class Answers(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer, default=0, primary_key=True)
    answer_body = db.Column(db.String, nullable = False)
    answ_votes = db.Column(db.String, default = 0)
    answered_by_user = db.Column(db.Integer, ForeignKey(User.username)) 
    accepted = db.Column(db.Boolean, default = False)
    user = db.relationship('User',  primaryjoin=(User.username == answered_by_user), lazy =True)


class Questions(db.Model):
    __tablename__ = 'questions'
    #qid = db.Column(db.Integer,default=mydefault(), primary_key = True)
    qid = db.Column(db.Integer,default = 0, nullable=False)
    title = db.Column(db.Text, nullable = False)
    __table_args__ = (
        PrimaryKeyConstraint('qid', 'title'),
    )
    question_body = db.Column(db.Text, nullable = False)
    answer_id = db.Column(db.Integer,ForeignKey('answers.answer_id'),default=0)
    asked_by_username = db.Column(db.String(30), ForeignKey(User.username))
    ques_votes = db.Column(db.Integer, default = 0)
    tag = db.Column(db.String(50), nullable = True)
    asked_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user = db.relationship('User', lazy = True, primaryjoin = (User.username == asked_by_username))
    answer = db.relationship('Answers', primaryjoin=(Answers.answer_id == answer_id), lazy = True)
    
    
class CommQuestions(db.Model):
    __tablename__ = 'comments_ques'
    cid = db.Column(db.Integer, primary_key=True)
    qid = db.Column(db.String(30), ForeignKey(Questions.qid))
    comment_by = db.Column(db.String(30), nullable=False)
    comment_body = db.Column(db.Text, nullable=False)
    question = db.relationship('Questions', primaryjoin=(Questions.qid == qid), lazy=True)

class CommAnswers(db.Model):
    __tablename__ = 'comments_ans'
    cid = db.Column(db.Integer, primary_key=True)
    aid = db.Column(db.String(30), ForeignKey(Answers.answer_id))
    comment_by = db.Column(db.String(30), nullable=False)
    comment_body = db.Column(db.Text, nullable=False)
    answer = db.relationship('Answers', primaryjoin=(Answers.answer_id == aid), lazy=True)

db.create_all()
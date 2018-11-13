from app import db
from datetime import datetime



class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    password = db.Column( db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable = False)
    reputation = db.Column( db.String, default = int(0))
    joined = db.Column(db.String, default = datetime.utcnow)
    profile_image = db.Column(db.String, default = None)
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{self.username}, {self.password}, {self.email}, {Self.reputation}, {self.joined}')"

db.create_all()
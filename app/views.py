from flask import render_template
from flask import url_for, redirect
# Import Request object to use
from flask import request
# from sqlalchemy import and_
from flask import url_for, redirect, request, make_response,flash
# Importing Session Object to use Sessions
from flask import session
# from app.models import User
from app import app , db
from app.models import User
from app.models import Questions
from app.models import Answers
from sqlalchemy import and_, Sequence
from sqlalchemy.sql import update
from sqlalchemy import create_engine
from sqlalchemy.sql import bindparam
from passlib.hash import pbkdf2_sha512



@app.route('/')
@app.route('/index')
def index():
	if 'user' in session:
		return render_template('index.html', logged_in = True)
	else:
		return render_template('index.html', logged_in = False)


# @app.route('/loginqanda')
# def Login_QandA():
# 	if 'user' in session:
# 		return render_template('index.html', logged_in = True)
# 	else:
# 		return render_template('index.html', logged_in = False)



@app.route('/login', methods=['POST', 'GET'])
def User_Login():
	userID = request.form['user']
	psswd = request.form['pass']
	
	user  = User.query.filter((User.username == userID)).first()
	if (user==None):
		return render_template("index.html", logged_in = False, auth_fail=True)
	if pbkdf2_sha512.verify(psswd,user.password):
		# flash('Login successful', 'success')
		session['user'] = userID
		remember_opt = request.form.get('remember-chk')
		if(remember_opt==None):
			session.permanent = False
		else:
			session.permanent = True
		return render_template('User_HomePage.html', username=user.display_name, logged_in = True, userinfo = user)
	return render_template("index.html", logged_in = False, auth_fail=True)

@app.route('/logoutqanda', methods=['POST', 'GET'])
def LogoutQandA():
	if 'user' in session:
		name = session.pop('user')
		# return render_template("QandA.html", logged_in = False)

	# else:
	return render_template("QandA.html", logged_in = False)

@app.route('/logoutaskques', methods=['POST', 'GET'])
def LogoutAsk():
	if 'user' in session:
		name = session.pop('user')
		# return render_template("QandA.html", logged_in = False)

	# else:
	return render_template("index.html", logged_in = False)

@app.route('/logoutuser', methods=['POST', 'GET'])
def LogoutUser():
	if 'user' in session:
		name = session.pop('user')
		return render_template("index.html", logged_in = False)

	else:
		return render_template("index.html")

@app.route('/userpage',methods=['POST'])
def User_HomePage():
	userinf = User.query.filter((User.username == session['user'])).first()
	return render_template('User_HomePage.html', logged_in=True, username=userinf.display_name, userinfo = userinf)

@app.route('/signup', methods=['POST'])
def Sign_Up():
	usrnm=request.form["username"]
	passwd=request.form['newpass']
	mail=request.form["email"]
	passphrase = pbkdf2_sha512.hash(passwd)
	user  = User.query.filter((User.username == usrnm)).first()
	if (user==None):
		user = User(username = usrnm,password=passphrase,display_name=usrnm,email=mail,)
		db.session.add(user)
		db.session.commit()
		# flash('Your account has been created! You are now able to log in', 'success')
		session['user'] = usrnm
		return render_template('User_HomePage.html', username=user.display_name,logged_in=True, userinfo=user)
	else:
		return render_template("index.html", logged_in = False, user_exists=True)

@app.route('/qanda',methods=['POST', 'GET'])
def QandA():
	if 'user' in session:
		return render_template('QandA.html', logged_in = True, username = session['user'])
	else:
		return render_template('QandA.html', logged_in = False)

@app.route('/askques',methods=['POST'])
def Ask_Ques():
	return render_template('Ask_Ques.html', username=session['user'])

@app.route('/askQuestion',methods=['POST'])
def Ask_Question():
	usrname=session['user']
	title = request.form['question_title']
	body = request.form['question_body']
	tag = request.form['question_tags']
	question = Questions(title = title,question_body=body,asked_by_username=usrname,tag=tag)
	db.session.add(question)
	db.session.commit()
	userinf = User.query.filter((User.username == session['user'])).first()
	return render_template('User_HomePage.html', username=userinf.display_name, userinfo = userinf)

@app.route('/about')
def About():
	return render_template('About.html')

@app.route('/coc')
def Answering_Policy():
	return render_template('Answering_Policy.html')

@app.route('/faq')
def FAQ():
	return render_template('FAQ.html')

@app.route('/updateprofile', methods=['POST'])
def Update_Profile():
	engine = create_engine('sqlite:///:memory:', echo=True)
	conn = engine.connect()
	user_name = session['user']
	dn=request.form['display_name']
	image=request.form['change_dp']
	bio=request.form['bio']
	# stmt = User.update().\
	#       values(display_name = dn).\
	# 	  where(User.username == bindparam('username'))
	# conn.execute(stmt,username = user_name)
	row = db.session.query(User).filter(User.username == user_name).first()
	row.display_name = dn
	row.bio = bio
	userinf = User.query.filter((User.username == session['user'])).first()
	return render_template('User_HomePage.html', username=userinf.display_name,logged_in=True,userinfo = userinf)

@app.route('/checklogin', methods=['POST'])
def CheckLogged_In():
	usrnm = request.form.get('user')
	user  = User.query.filter((User.username == usrnm)).first()
	if (user==None):
		return 'true'
	else:
		return 'false'

@app.errorhandler(404)
def http_404_handler(error):
	return render_template('Error404.html')

@app.errorhandler(405)
def http_405_handler(error):
	return render_template('Error405.html')

@app.errorhandler(500)
def internal_error_handler(error):
    db.session.rollback()
    return render_template('Error500.html')
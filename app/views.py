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
from sqlalchemy import and_
from passlib.hash import pbkdf2_sha512

@app.route('/')
@app.route('/index')
def index():
	if 'user' in session:
		return render_template('index.html', logged_in = True)
	else:
		return render_template('index.html', logged_in = False)



@app.route('/login', methods=['POST', 'GET'])
def User_Login():
	userID = request.form['user']
	psswd = request.form['pass']
	
	user  = User.query.filter((User.username == userID)).first()
	if pbkdf2_sha512.verify(psswd,user.password):
		# flash('Login successful', 'success')
		session['user'] = userID
		remember_opt = request.form.get('remember-chk')
		if(remember_opt==None):
			session.permanent = False
		else:
			session.permanent = True
		return render_template('User_HomePage.html', username=session['user'], logged_in = True)
	return render_template("index.html", logged_in = False)

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
	return render_template('User_HomePage.html', logged_in=True, username=session['user'])

@app.route('/signup', methods=['POST'])
def Sign_Up():
	usrnm=request.form["username"]
	passwd=request.form['newpass']
	mail=request.form["email"]
	passphrase = pbkdf2_sha512.hash(passwd)
	user = User(username = usrnm,password=passphrase,display_name=usrnm,email=mail,)
	db.session.add(user)
	db.session.commit()
	flash('Your account has been created! You are now able to log in', 'success')
	return render_template('User_HomePage.html', logged_in=True)

@app.route('/qanda',methods=['POST', 'GET'])
def QandA():
	if 'user' in session:
		return render_template('QandA.html', logged_in = True, username = session['user'])
	else:
		return render_template('QandA.html', logged_in = False)

@app.route('/askques',methods=['POST'])
def Ask_Question():
	return render_template('Ask_Ques.html', username=session['user'])

@app.route('/about')
def About():
	return render_template('About.html')

@app.route('/coc')
def Answering_Policy():
	return render_template('Answering_Policy.html')

@app.route('/updateprofile')
def Update_Profile():
	#write dbms code here
	return render_template('User_HomePage.html', logged_in=True)

# @app.route('/checklogin', methods=['POST', 'GET'])
# def CheckLogged_In():
# 	if 'user' in session:
# 		return 'true'
# 	else:
# 		return 'false'


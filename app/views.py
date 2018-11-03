from flask import render_template
from flask import url_for, redirect
# Import Request object to use
from flask import request

from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/User_HomePage')
def User_HomePage():
	return render_template('User_HomePage.html')

@app.route('/QandA')
def QandA():
	return render_template('QandA.html')

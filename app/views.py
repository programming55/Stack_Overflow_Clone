from flask import render_template
from flask import url_for, redirect
# Import Request object to use
from flask import request

from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/userpage')
def User_HomePage():
	return render_template('User_HomePage.html')

@app.route('/qanda')
def QandA():
	return render_template('QandA.html')

@app.route('/about')
def About():
	return render_template('About.html')

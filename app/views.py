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
from base64 import b64encode
from sqlalchemy import desc
# from sqlalchemy import inspect
# import sqlite3
import pickle

# conn = sqlite3.connect('IIITHSO.db')

with open('objs.pkl','rb') as f: 
     index_ans_id,index_qid = pickle.load(f)

def mydefault():
    global index_qid
    index_qid += 1
    return index_qid

def AnswerId():
    global index_ans_id
    index_ans_id+=1
    return index_ans_id

with open('objs.pkl', 'wb') as f: 
    pickle.dump([index_ans_id, index_qid], f)

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
		userinf = User.query.filter((User.username == session['user'])).first()
		pic2 = None
		if userinf.profile_image_data != None:
			pic = b64encode(userinf.profile_image_data)
			pic2 = pic.decode('ascii')
		return render_template('User_HomePage.html', username=user.display_name, logged_in = True, userinfo = user, image=pic2)
	return render_template("index.html", logged_in = False, auth_fail=True)

@app.route('/logoutqanda', methods=['POST', 'GET'])
def LogoutQandA():
	if 'user' in session:
		name = session.pop('user')
		# return render_template("QandA.html", logged_in = False)

	# else:
	return render_template("index.html", logged_in = False)

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
	pic = b64encode(userinf.profile_image_data)
	pic2 = pic.decode('ascii')
	return render_template('User_HomePage.html', logged_in=True, username=userinf.display_name, userinfo = userinf, image=pic2)

@app.route('/signup', methods=['POST'])
def Sign_Up():
	usrnm=request.form["username"]
	passwd=request.form['newpass']
	mail=request.form["email"]
	passphrase = pbkdf2_sha512.hash(passwd)
	file = open("app/static/images/generic_avatar.png","rb")
	user  = User.query.filter((User.username == usrnm)).first()
	if (user==None):
		user = User(username = usrnm,password=passphrase,display_name=usrnm,email=mail,profile_image="generic_avatar", profile_image_data=file.read(),)
		db.session.add(user)
		db.session.commit()
		# flash('Your account has been created! You are now able to log in', 'success')
		session['user'] = usrnm
		pic = b64encode(user.profile_image_data)
		pic2 = pic.decode('ascii')
		return render_template('User_HomePage.html', username=user.display_name,logged_in=True, userinfo=user,image=pic2)
	else:
		return render_template("index.html", logged_in = False, user_exists=True)

# @app.route('/qanda',methods=['GET'])
# def Ques():
# 	if 'user' in session:
# 		return render_template('QandA.html', logged_in = True, username = session['user'])
# 	else:
# 		return render_template('QandA.html', logged_in = False)

@app.route('/qanda/<title>',methods=['POST', 'GET'])
def QandA(title):
	question = Questions.query.filter_by(title=title).first()
	asked_by = User.query.filter_by(username=question.asked_by_username).first()
	# user_name =session['user']
	show_ans = db.session.query(Answers).join(Questions).filter(Questions.answer_id == Answers.answer_id , Questions.title==title).order_by(desc(Answers.accepted)).all()
	pic2 = None
	if asked_by.profile_image_data != None:
		pic = b64encode(asked_by.profile_image_data)
		pic2 = pic.decode('ascii')
	if 'user' in session:
		return render_template('QandA.html', logged_in = True, username = session['user'], ques=question, image=pic2, user = asked_by, ansr=show_ans)
	else:
		return render_template('QandA.html', logged_in = False, ques=question, user = asked_by, image=pic2, ansr=show_ans)

@app.route('/askques',methods=['POST'])
def Ask_Ques():
	return render_template('Ask_Ques.html', username=session['user'])

@app.route('/askQuestion',methods=['POST'])
def Ask_Question():
	usrname=session['user']
	title = request.form['question_title']
	body = request.form['question_body']
	tag = request.form['question_tags']
	question = Questions(title = title,qid=mydefault(), question_body=body,asked_by_username=usrname,tag=tag)
	db.session.add(question)
	db.session.commit()
	userinf = User.query.filter((User.username == session['user'])).first()
	pic2 = None
	if userinf.profile_image_data != None:
		pic = b64encode(userinf.profile_image_data)
		pic2 = pic.decode('ascii')
	return render_template('User_HomePage.html', username=userinf.display_name, userinfo = userinf,image=pic2)

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
	file = request.files['change_dp']
	bio=request.form['bio']
	row_changed = User.query.filter_by(username=user_name).update(dict(user_bio = bio, display_name=dn,profile_image=file.filename, profile_image_data=file.read()))
	db.session.commit()
	userinf = User.query.filter((User.username == session['user'])).first()
	pic = b64encode(userinf.profile_image_data)
	pic2 = pic.decode('ascii')
	return render_template('User_HomePage.html', username=userinf.display_name, image=pic2 ,logged_in=True,userinfo = userinf)

@app.route('/checklogin', methods=['POST'])
def CheckLogged_In():
	usrnm = request.form.get('user')
	user  = User.query.filter((User.username == usrnm)).first()
	if (user==None):
		return 'true'
	else:
		return 'false'

@app.route('/searchtitle', methods=['POST'])
def Search_Title():
	ques_title = request.form['ques_by_title']
	results = Questions.query.filter(Questions.title.ilike('%'+ques_title+'%')).all()
	if 'user' in session:
		return render_template('Search_Results.html', logged_in = True, srchbyques=results)
	else:
		return render_template('Search_Results.html', logged_in = False, srchbyques=results)

@app.route('/searchtag', methods=['POST'])
def Search_Tag():
	ques_tag = request.form['ques_by_tag']
	results = Questions.query.filter(Questions.tag.ilike(ques_tag), Questions.answer_id==0).all()
	if 'user' in session:
		return render_template('Search_Results.html', logged_in = True, srchbyques=results)
	else:
		return render_template('Search_Results.html', logged_in = False, srchbyques=results)

@app.route('/top10ques')
def getTop10ques():
	quest = Questions.query.filter(Questions.answer_id==0).limit(10).all()
	if 'user' in session:
		return render_template('index.html', logged_in = True, ques = quest)
	else:
		return render_template('index.html', logged_in = False, ques = quest) 

# @app.route('/upvote_ques', methods=['POST'])
# def upvote_ques():
# 	user_name = session['user']
# 	title = request.url()
# 	qtitle = title.split("/")[2]
# 	show_ans = db.session.query(Answers).join(Questions).filter(Questions.asked_by_username == user_name,  Questions.answer_id == Answers.answer_id).all()
# 	v_query = db.session.query(Questions).join(User).filter(Questions.title == title).first()
# 	new_votes = vote_query.ques_votes+10
# 	changed_row = Questions.query.filter(Questions.title==vote_query.title).update(dict(vote_query.ques_votes = new_votes))
# 	db.session.commit()


# @app.route('/downvote_ques')
# def downvote_ques():
# 	user_name = session['user']
# 	title = request.url()
# 	title = title.split("/")[2]
# 	vote_query = query(Questions).join(User).filter_by(Questions.title == title).first()
# 	new_votes = vote_query.ques_votes-10
# 	row_changed = Questions.query.filter_by(title=vote_query.title).update(dict(vote_query.ques_votes = new_votes))
# 	db.session.commit()


# @app.route('/upvote_ans/aid')
# def upvote_ans():
	

# @app.route('/downvote_ans')


# @app.route('/activity')
# def showActivity():
# 	user_name = session['user']
# 	ques_asked = User.query.join(Questions).filter_by(User.username == user_name).first()
# 	return render_template('User_HomePage.html',ques = ques_asked, logged_in=True)


@app.route('/postans/<title>', methods=['POST'])
def Post_Answer(title):
	new_ans_id = AnswerId()
	user = session['user']
	reqd = Questions.query.filter((Questions.title == title)).first()
	row_updated = Questions(qid=mydefault(), title=reqd.title, question_body=reqd.question_body,answer_id= new_ans_id, asked_by_username=reqd.asked_by_username)
	db.session.add(row_updated)
	db.session.commit()
	answer = request.form["answer-body"]
	answer_updated = Answers(answer_id=new_ans_id, answer_body=answer,answered_by_user=user)
	db.session.add(answer_updated)
	db.session.commit()
	return render_template('index.html', logged_in = True)


@app.route('/acceptans', methods=['POST'])
def Accept_Ans():
	ansid = request.form.get('ans_id')
	row_change= Answers.query.filter(Answers.answer_id == ansid).update(dict(accepted = 1))
	db.session.commit()
	return "true"

@app.route('/ansaccepted', methods=['POST'])
def Ans_Accepted():
	ansid = request.form.get('ans_id')
	accept = Answers.query.filter(Answers.answer_id == ansid).first()
	if (accept.accepted == 1):
		return "true"
	else:
		return "false"


# @app.route('/comment_ques')
# def commentQuestion():
# 	usrname=session['user']
# 	title = request.url()
#     ques_title = title.split("/")[2]
# 	#adding a new row to CommQuestions table
# 	comment_ques = CommQuestions(q_title=ques_title, cid=commQues(),comment_by=usrname, comment_body=ques_comment)
# 	db.session.add(comment)
# 	db.session.commit()

# @app.route('/comment_answer')
# def commentAnswer():
# 	usrname=session['user']
# 	#get answer_id from innerHTML
#     rcvd_ans_id = #...............
# 	#adding a new row to CommAnswers table
# 	comment_ans = CommAnswers(cid=commAns(),aid=rcvd_ans_id,comment_by=usrname, comment_body=ans_comment)
# 	db.session.add(comment)
# 	db.session.commit()	


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
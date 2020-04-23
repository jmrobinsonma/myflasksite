from flask import render_template,url_for
from app import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/myscrapbook')
def myscrapbook():
	return render_template('mynotebook.html')

@app.route('/freestuff_app_book')
def freestuff_app_book():
	return render_template('freestuff_app_book.html')

@app.route('/dicebook')
def dicebook():
	return render_template('dicebook.html')

@app.route('/apibook')
def apibook():
    return render_template('apibook.html')

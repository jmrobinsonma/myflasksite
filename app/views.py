from flask import render_template,url_for
from app import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/myscrapbook')
def myscrapbook():
	return render_template('mynotebook.html')
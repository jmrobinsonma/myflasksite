import requests
import json
from flask import render_template,url_for
from app import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

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

@app.route('/flasksitebook')
def flasksitebook():
	return render_template('flasksitebook.html')

@app.route('/spacex_launch_data')
def spacex_launch_data():
	url = "https://api.spacexdata.com/v3/launches/latest"
	response = requests.get(url)
	result = json.loads(response.text)
	return render_template('spacex_launch_data.html', result=result, url=url)


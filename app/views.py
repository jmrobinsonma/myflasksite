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

@app.route('/lasttenresults')
def lasttenresults():
    results = requests.get('http://localhost:5001/last-ten')
    return render_template('lasttenresults.html', results=json.loads(results.text))


from flask import render_template
from app import app

@app.route('/')
def mynotebook_page():
	return render_template('mynotebook.html')
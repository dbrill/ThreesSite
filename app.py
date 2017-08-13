from flask import Flask, render_template
from datetime import datetime
from os import environ
import sys
app = Flask(__name__)

@app.route('/')
def homepage():
	print ('hello')
	print environ.get('DATABASE_URL')
	return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

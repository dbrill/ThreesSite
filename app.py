from __future__ import print_function
from flask import Flask, render_template
from datetime import datetime
from os import environ
import sys
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/hdox')
def hdoxPage():
    return render_template('hdox.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

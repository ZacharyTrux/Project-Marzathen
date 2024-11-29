from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/developerInfo.html')
def secret():
    return render_template('developerInfo.html')

if __name__ == '__main__':
    app.run(debug=True)

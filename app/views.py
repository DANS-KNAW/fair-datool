from flask import Flask, render_template
from PIL import Image
from flask import send_file
from app import app

@app.route("/")
def indexpage():
    return 'Badge'

@app.route("/star")
def star():
    path = "../app/static/star.png"
    return send_file(path, mimetype='image/png')

@app.route("/fair")
def fair():
    path = "../app/static/fairdatool.png"
    return send_file(path, mimetype='image/png')

@app.route('/tool')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

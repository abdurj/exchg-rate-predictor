from flask import render_template, request, redirect, url_for
from app import app
import random

@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    lis = []
    if(request.method == 'POST'):
        string = request.form['headline']
        #TODO:  Replace random numbers with return from program
        for x in range(6):
            lis.append(random.randint(-5,5))
        return render_template('output.html', output = lis)
    return render_template('index.html')

@app.route('/output', methods=['GET'])
def output():
    if request.method == "GET":
        if request.form.get("reset") == "Reset":
            print("Reset")
            return redirect(url_for('index'))
    return render_template('output.html')

@app.route('/button')
def button():
    return render_template('index.html')
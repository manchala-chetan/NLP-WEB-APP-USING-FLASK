from flask import Flask, render_template, request, redirect, session
import api
from db import Database
from config import Config

'''
app.run(debug=True) helps us when if any changes are made in the program, it automatically
restarts the server and runs the program. if we just use app.run(), we need to run the program
again and again to see the changes that u have made to the program.
'''

### Routes are like URLS where we cantype it and redirect to that page

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message='Registration Successful. Kindly Login to Proceed')
    else:
        return render_template('register.html',message = 'Email Already Exists')


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect email/password')

@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html')
    return redirect('/')

@app.route('/ner')
def ner():
    if 'logged_in' in session:
        return render_template('ner.html')
    return redirect('/')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    if 'logged_in' in session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        return render_template('ner.html', response=response)
    return redirect('/')

@app.route('/sentiment')
def sentiment():
    if 'logged_in' in session:
        return render_template('sentiment.html')
    return redirect('/')

@app.route('/abuse')
def abuse():
    if 'logged_in' in session:
        return render_template('abuse.html')
    return redirect('/')

@app.route('/perform_sentiment', methods=['post'])
def perform_sentiment():
    if 'logged_in' in session:
        text = request.form.get('sentiment_text')
        response = api.sentiment_analysis(text)
        return render_template('sentiment.html', response=response)
    return redirect('/')

@app.route('/perform_abuse_detection', methods=['post'])
def perform_abuse_detection():
    if 'logged_in' in session:
        text = request.form.get('abuse_text')
        response = api.abuse_detection(text)
        return render_template('abuse.html', response=response)
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')


app.run(debug=True)


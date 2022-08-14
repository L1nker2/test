from flask import Flask
from flask import render_template
from flask import request


app=Flask(__name__)


@app.route("/")
@app.route('/index')
@app.route('/index.html')
def one():
    return render_template('index.html')


@app.route('/secret')
@app.route('/secret.html')
def sec():
    return render_template('secret.html')


@app.route('/login.html', methods=['POST','GET'])
def log():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        key=request.form.get('key')
        if key=='9218450123412':
            return render_template('goodwork.html')
        else:
            return render_template('oops.html')


@app.route('/oops.html')
def o():
    return render_template('oops.html')


@app.route('/secretkey.html')
@app.route('/secretkey')
def s():
    return render_template('secretkey.html')



app.run()
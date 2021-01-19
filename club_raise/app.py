from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def usermain():
    return render_template('usermain.html')

@app.route("/userlogin")
def login():
    return render_template('userlogin.html')

@app.route("/rootlogin")
def join():
    return render_template('rootlogin.html')

@app.route("/registered")
def registered():
    return render_template('registered.html')

@app.route("/root")
def root():
    return render_template('rootmain.html')


if __name__ == '__main__':
    app.run(debug=True)
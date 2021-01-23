from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def usermain():
    return render_template('usermain.html')


@app.route("/login")
def login():
    return render_template('loginmax.html')

@app.route("/join")
def join():
    return render_template('join.html')

@app.route("/root")
def root():
    return render_template('root.html')


if __name__ == '__main__':
    app.run(debug=True)
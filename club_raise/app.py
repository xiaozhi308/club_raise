import random
from datetime import timedelta

import user_db, root_db
from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route("/")
def usermain():
    return render_template('usermain.html')

@app.route("/userlogin")
def userlogin():
    return render_template('userlogin.html')

@app.route("/loginma", methods=["POST"])
def loginma():
    if request.method == "POST":
        username = request.form.get("username")
        userpasswd = request.form.get("userpasswd")
        ls = [username]
        us = user_db.session.execute("select user_passwd from user where  user_name = %s;", ls)
        session['username'] = username
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1)

        for i in us:
            if i[0] == userpasswd:
                print(username + userpasswd)
                print(i[0])
                print(i)
                print("000000000000")
                return redirect(url_for('usermain'))
            else:
                print(username + userpasswd)
                print(i[0])
                print(i)
                print("1111111111111111")
                return redirect(url_for('userlogin'))

    if request.method == "GET":
        return render_template("userlogin.html")


@app.route("/regis", methods=["GET", "POST"])
def regis():
    if request.method == "GET":
        return render_template('registered.html')
    if request.method == "POST":
        telephone = request.form.get("telephone")
        username = request.form.get("username")
        userpasswd = request.form.get("userpasswd")
        quserpasswd = request.form.get("quserpasswd")
        if userpasswd == quserpasswd:
            lsname = []
            lsname.append(username)
            lspass = []
            lspass.append(telephone)
            x = user_db.ressult(lsname, lspass)
            if x == 0:
                ls = [username, userpasswd, telephone]
                user_db.session.execute("INSERT INTO user ( user_name , user_passwd ,user_phone_number ) VALUES (%s , %s , %s );", ls)
                print("11111111111")
                return render_template("userlogin.html")
            else:
                print("22222222")
                return render_template("registered.html")
        else:
            print("333333333333")
            return render_template("registered.html")


@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'login_user': user}
    return {}

@app.context_processor
def root_context_processor():
    root = session.get('rootname')
    if root:
        return {'login_root': root}
    return {}

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('usermain'))


@app.route("/rootlogin")
def rootlogin():
    return render_template('rootlogin.html')


@app.route("/rootloginre")
def rootloginre():
    if request.method == "POST":
        rootname = request.form.get("rootname")
        rootpasswd = request.form.get("rootpasswd")
        ls = [rootname]
        us = user_db.session.execute("select root_passwd from user where root_name = %s;", ls)
        session['rootname'] = rootname
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1)

        for i in us:
            if i[0] == rootpasswd:
                print(rootname + rootpasswd)
                print(i[0])
                print(i)
                print("000000000000")
                return redirect(url_for('rootmain'))
            else:
                print(rootname + rootpasswd)
                print(i[0])
                print(i)
                print("1111111111111111")
                return redirect(url_for('rootlogin'))

    if request.method == "GET":
        return render_template("userlogin.html")
    return render_template('rootlogin.html')


@app.route("/userre")
def userre():
    return render_template('registered.html')


@app.route("/root")
def root():
    return render_template('rootmain.html')


if __name__ == '__main__':
    app.run(debug=True)
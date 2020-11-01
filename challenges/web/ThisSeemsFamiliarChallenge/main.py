import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = 'kfji1fj390jf9afj91jf09j19fjakjfg0'

app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")

db = MySQL(app)
currentUser = None
handler = 1
failed = 0

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/studLogin', methods=['GET', 'POST'])
def studLogin():
    global failed, handler
    failed = 0
    handler = 1
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            uname = request.form['username']
            pword = request.form['password']

            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            #  1 OR 1=1;")#
            cursor.execute(
                f"SELECT * FROM users WHERE username={uname} AND password=%s", (pword, ))
            info = cursor.fetchone()

            if info is not None:
                cursor.execute(
                    f"SELECT users.username FROM users WHERE username={uname}")
                app.register_error_handler(500, error)

                user = cursor.fetchone()
                if user['username'] == "45678909":
                    session['student_user'] = user['username']
                else:
                    failed = 1
                    return render_template("studLogin.html", failed=failed)

                global currentUser
                currentUser = user['username']

                return redirect(url_for('home'))
            else:
                failed = 1
                return render_template("studLogin.html", failed=failed)
    return render_template("studLogin.html", failed=failed)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if studentLoggedIn(session):
        return render_template("home.html", currentUser=currentUser)
    else:
        return redirect(url_for('studLogin'))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('student_user')
    session.pop('staff_user')
    return redirect(url_for('studLogin'))


@app.route('/staff', methods=['GET', 'POST'])
def staff():
    global failed, handler
    failed = 0
    handler = 0
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            uname = request.form['username']
            pword = request.form['password']

            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            #  1 OR 1=1;")#
            cursor.execute(
                f"SELECT * FROM users WHERE username={uname} AND password=%s", (pword, ))
            info = cursor.fetchone()

            if info is not None:
                cursor.execute(
                    f"SELECT users.username FROM users WHERE username={uname}")
                app.register_error_handler(500, error)

                user = cursor.fetchone()
                if user['username'] == "98765432":
                    session['staff_user'] = user['username']
                else:
                    failed = 1
                    return render_template("staff.html", failed=failed)

                global currentUser
                currentUser = user['username']

                return redirect(url_for('staffHome'))
            else:
                failed = 1
                return render_template("staff.html", failed=failed)
    return render_template("staff.html", failed=failed)


@app.route('/staffHome', methods=['GET', 'POST'])
def staffHome():
    if staffLoggedIn(session):
        return render_template("staffHome.html", currentUser=currentUser)
    else:
        return redirect(url_for('staff'))


@app.route('/comp3850', methods=['GET', 'POST'])
def comp3850():
    if studentLoggedIn(session) or staffLoggedIn(session):
        return render_template("comp3850.html", currentUser=currentUser)
    else:
        return redirect(url_for('studLogin'))


@app.route('/compstaff', methods=['GET', 'POST'])
def compstaff():
    if studentLoggedIn(session) or staffLoggedIn(session):
        return render_template("compstaff.html", currentUser=currentUser)
    else:
        return redirect(url_for('studLogin'))


@app.route('/gradebook', methods=['GET', 'POST'])
def gradebook():
    if staffLoggedIn(session):
        if request.method == 'POST':
            if 'flagPassword' in request.form:
                flag = request.form['flagPassword']
                if flag == "b1naryb0mb":
                    return redirect(url_for('success'))
        return render_template("gradebook.html", currentUser=currentUser)
    else:
        return redirect(url_for('staff'))


@app.route('/passwordSpecifications', methods=['GET', 'POST'])
def passwordSpecifications():
    if staffLoggedIn(session):
        return render_template("passwordSpecs.html", currentUser=currentUser)
    else:
        return redirect(url_for('staffLogin'))


@app.route('/success', methods=['GET', 'POST'])
def success():
    if studentLoggedIn(session) or staffLoggedIn(session):
        return render_template("success.html")
    else:
        return redirect(url_for('studLogin'))


@app.errorhandler(500)
def error(e):
    if handler == 1:
        failed = 1
        return render_template("studLogin.html", failed=failed)
    else:
        failed = 1
        return render_template("staff.html", failed=failed)


def studentLoggedIn(session):
    try:
        if session['student_user']:
            return True
    except KeyError:
        return False


def staffLoggedIn(session):
    try:
        if session['staff_user']:
            return True
    except KeyError:
        return False


if __name__ == '__main__':
    app.run(debug=False)

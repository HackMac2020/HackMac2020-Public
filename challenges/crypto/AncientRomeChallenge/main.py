import string
import collections
from random import randrange
from flask import Flask, render_template, redirect, url_for, request

hidden = 'hackerman'
i=0

app = Flask(__name__)


def caesar():
    move = randrange(26)
    if move == 0:
        move = randrange(26)
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(move)
    lower.rotate(move)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return(hidden.translate(str.maketrans(string.ascii_lowercase, lower)).translate(str.maketrans(string.ascii_uppercase, upper)))


@app.route('/', methods=['GET', 'POST'])
def index():
    global i
    i += 1
    ciphertext = caesar()
    if request.method == 'POST':
        if request.form['answer'] == hidden:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('incorrect'))
    return render_template("index.html", ciphertext=ciphertext)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html")


@app.route('/incorrect', methods=['GET', 'POST'])
def incorrect():
    return render_template("incorrect.html")


if __name__ == '__main__':
    app.run(debug=True)

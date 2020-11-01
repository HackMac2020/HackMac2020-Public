from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/stage1', methods=['GET', 'POST'])
def stage1():
    failed = 0
    if request.method == 'POST':
        if request.form['answer'] is not None:
            if request.form['answer'] == "Germany":
                return redirect(url_for('stage2'))
            else:
                failed = 1
                return render_template("stage1.html", failed=failed)
    return render_template("stage1.html", failed=failed)


@app.route('/stage2', methods=['GET', 'POST'])
def stage2():
    failed = 0
    if request.method == 'POST':
        if request.form['answer'] is not None:
            if request.form['answer'].lower() == "jamaica":
                return redirect(url_for('stage3'))
            else:
                failed = 1
                return render_template("stage2.html", failed=failed)
    return render_template("stage2.html", failed=failed)


@app.route('/stage3', methods=['GET', 'POST'])
def stage3():
    failed = 0
    if request.method == 'POST':
        if request.form['answer'] is not None:
            if request.form['answer'] == "Afghanistan":
                return redirect(url_for('stage4'))
            else:
                failed = 1
                return render_template("stage3.html", failed=failed)
    return render_template("stage3.html", failed=failed)


@app.route('/stage4', methods=['GET', 'POST'])
def stage4():
    failed = 0
    if request.method == 'POST':
        if request.form['answer'] is not None:
            if request.form['answer'] == "Indonesia" or "indonesia":
                return redirect(url_for('success'))
            else:
                failed = 1
                return render_template("stage4.html", failed=failed)
    return render_template("stage4.html", failed=failed)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)

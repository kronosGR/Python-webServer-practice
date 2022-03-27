from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/about')
def about():
    return render_template('./about.html')


@app.route('/<username>')
def user(username=None):
    return render_template('index.html', name=username)

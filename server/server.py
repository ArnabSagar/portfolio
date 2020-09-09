from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')  #decorator
def hello_world(username=None, post_id = None):
    return render_template('index.html', name=username, post_id=post_id)


# @app.route('/favicon.ico')
# def blog():
#     return 'what@ss'

@app.route('/blog/of/my/dog')
def dogs():
    return "my doggo!"
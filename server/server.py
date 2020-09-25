from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.pdf')

# @app.route('/favsicon.ico')
# def blog():
#     return 'what@ss'

@app.route('/blog')
def dogs():
    return "blog page"
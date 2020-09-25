from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)
print(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/resume')
def resume(filename = None):
    with open('./static/Sagar_Arnab_F20.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename="Sagar_Arnab_F20.pdf")
# @app.route('/favsicon.ico')
# def blog():
#     return 'what@ss'

@app.route('/blog')
def dogs():
    return "blog page"
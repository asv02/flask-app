from flask_app import app
from flask import render_template,request,redirect,url_for
@app.route('/')
def home():
    value1 = 20
    value2 = "Template value2"
    return render_template('home.html',value1=value1,value2=value2)

@app.route('/api/auth/login')
def login():
    greet = request.args.get('greet')
    return str(dir(request))

@app.template_filter('reverse_string')
def reverseString(s):
    return s[::-1]

@app.route('/other_dynamic_url')
def other():
    return "Dynamic URL Endpoint"

@app.route('/redirect_other_url')
def redirect_url():
    return redirect(url_for('other'))

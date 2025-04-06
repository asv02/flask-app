from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/auth/login')
def login():
    greet = request.args.get('greet')
    return str(dir(request))


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5500)
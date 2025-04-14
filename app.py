from flask import Flask, request, render_template,redirect,url_for,Response
import pandas as pd
app = Flask(__name__,template_folder='templates')

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
    return render_template('index.html')


@app.route('/redirect_other_url')
def redirect_url():
    return redirect(url_for('other'))

@app.route('/login_page',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        if(username == 'akash') and (password=='qwerty'):
            return redirect(url_for('other'))

@app.route('/file_upload', methods=['GET','POST'])
def file_uploading():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df  =  pd.read_excel(file)
        return df.to_html()
    
@app.route('/file_download',methods = ['GET','POST'])
def file_downloading():
    file = request.files['file']
    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype = 'text/csv',
        headers = {
            'Content-Disposition':'attachment; filename=result.csv'
        }
    )
    return response


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5500)
from flask import Flask,request,render_template

app = Flask(__name__)
#python27的flask和jinja2里面的capy.py需要手动复制进去！
@app.route('/', methods=(['GET','POST']))
def home():
    return render_template('home.html')

@app.route('/signin',methods=(['GET']))
def signin_form():
    return render_template(('form.html'))

@app.route('/signin',methods=(['POST']))
def signin():
    username = request.form('username')
    password = request.form('password')
    if username == 'admin' and password == 'password':
        return render_template('signin.html')
    else:
        return render_template('form.html',message = 'Bad username or password',username = username)

if __name__ == '__main__':
    app.run()

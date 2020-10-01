"""

To display my name on Browser using python


"""
import flask
from flask import Flask,render_template

myapp = Flask(__name__,template_folder ='Template')

@myapp.route('/index')
def Display():
    return ("<h1>Welcome </h1> to my first web demo created using python")

@myapp.route('/<name>')
def Hello(name):
    return ("Hello <h1>name</h1>How are you doing ? ")

@myapp.route('/Mypage')
def MyPage():
    return render_template('MyPage.html')

if __name__ == '__main__':
    myapp.run()

from flask import Flask
from flask import request

#WA[
from whatsapp import Client
expected_token = 'precursive100'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
def sendmsg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    loginExt = request.args.get('login')
    passwordExt = request.args.get('password')
    if(str(token) == expected_token):
        client = Client(login=loginExt, password=passwordExt)
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    app.run()
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
    res = ''
    to = request.args.get('to')
    res +=to +'/'
    msg = request.args.get('msg')
    res +=msg +'/'
    if(str(token) == expected_token):
        client = Client(login='48664972472', password='yJD1iH6HI20rICObDuNTKFu3Mrs=')
        res += str(client.send_message(to, msg)) 
    
    else:
        res = 'Unauthorized'
    
    return res

if __name__ == '__main__':
    app.run()
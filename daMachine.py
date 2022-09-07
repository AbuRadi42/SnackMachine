from flask import Flask, render_template, request
from datetime import datetime


import json, random

App = Flask(__name__)

theWallet = {
    '_10c': random.randint(0, 9),
    '_20c': random.randint(0, 9),
    '_50c': random.randint(0, 9),
    '_$1': random.randint(0, 9),
    '_$20': random.randint(0, 5),
    '_$50': random.randint(0, 2)
}

@App.get('/')
def index():

    return render_template('index.html')

@App.get('/checkTheWallet')
def checkTheWallet():

    res = App.response_class(
        response = json.dumps(theWallet),
        mimetype = 'application/json'
    )

    return res

@App.post('/subtractMoney')
def subtractMoney():

    if not request.json['Type'] or theWallet[request.json['Type']] == 0:

        return {'response': 'KO'}

    else:

        theWallet[request.json['Type']] -= 1

        return {'response': 'OK'}

@App.post('/returnChange')
def returnChange():

    if not request.json['Type'] or theWallet[request.json['Type']] == 0:

        return {'response': 'KO'}

    else:

        theWallet[request.json['Type']] -= 1

        return {'response': 'OK'}

if __name__ == '__main__':

    App.run(host = '0.0.0.0', port = 6789, debug = True, use_reloader = True)
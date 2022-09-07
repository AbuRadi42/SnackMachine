from flask import Flask, render_template, request
from flask_cors import CORS
from datetime import datetime

import json, random, string

App = Flask(__name__)

CORS(App)

sessions = {}

theWallet = {
    '_10c': random.randint(0, 9),
    '_20c': random.randint(0, 9),
    '_50c': random.randint(0, 9),
    '_$1': random.randint(0, 9),
    '_$20': random.randint(0, 5),
    '_$50': random.randint(0, 2)
}

# an alternative implementation:

# class theWallet:

#     _10c = random.randint(0, 9)
#     _20c = random.randint(0, 9)
#     _50c = random.randint(0, 9)
#     _US1 random.randint(0, 9)
#     _US20 random.randint(0, 5)
#     _US50 random.randint(0, 2)

# & yet, with many users:

@App.get('/')
def index():

    token = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))

    # return render_template('index.html')

    sessions[token] = {
        'wallet': {
            '_10c': random.randint(0, 9),
            '_20c': random.randint(0, 9),
            '_50c': random.randint(0, 9),
            '_$1': random.randint(0, 9),
            '_$20': random.randint(0, 5),
            '_$50': random.randint(0, 2)
        },
        'events': [] # to add a feature for recording sales
    }

    return {
        'response': 'OK',
        'session': token
    }

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

    if not request.json['Amount']:

        return {'response': 'KO'}

    else:

        C = round(float(request.json['Amount']), 2)

        if (1):

            return 1

        return {'response': 'OK'}

if __name__ == '__main__':

    App.run(host = '0.0.0.0', port = 6789, debug = True, use_reloader = True)
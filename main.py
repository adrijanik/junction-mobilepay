# -*- coding:utf8 -*-
# !/usr/bin/env python

import json
from datetime import datetime
from flask import Flask, request, make_response, jsonify
import get_contacts as phone

app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook

    """
    print("RECEIVED")
    req = json.loads(request.json)#
#    req = get_json(silent=True, force=True)
    print(req)
    print(type(req))
    res = "How can I help you?"
    try:
        action = req['result']['action']#
#        action = req.get('result').get('action')
    except AttributeError as e:
        print("ERRRROR JSON")
        print(e)
        return 'json error'

    if action == 'transfer.money':
        res = friend_transfer(req)
    if action == 'transfer.money.yes':
        for x in req['result']['contexts']:
            if x['name'] == 'transfermoney-followup':
                currency = x['parameters']['amount'][0]['currency']
                amount = x['parameters']['amount'][0]['amount']
                contact = x['parameters']['contact'][0]

        res = "Payed {}{} to {}".format(amount,currency,contact)
        contacts = phone.get_contacts()
        guesses = [(x, contacts[x]['name'], contacts[x]['phone']) for x in contacts]
        for guess in guesses:
            if contact == guess[1]:

                with open('history.log','a') as f:
                    f.write('\n'+' '.join([str(datetime.now()),str(amount),currency,contact,guess[0],guess[2]]))
            
#        res = friend_transfer(req)

  
#    if action == 'transfer.money.yes.transfermoney-yes-yes':
#        res = "Payed!"

    print(res)


    return jsonify({'speech':res})

def handle_money(params):
    print("Handle money")
    tmp = params['contexts']
    currency = "NN"
    amount = "NN"
    contact = "NN"
    contacts = phone.get_contacts()
    guesses = [(x, contacts[x]['name'], contacts[x]['phone']) for x in contacts]
    for x in tmp:
        if x['name'] == 'transfermoney-followup':
            currency = x['parameters']['amount'][0]['currency']
            amount = x['parameters']['amount'][0]['amount']
            contact = x['parameters']['contact'][0]

    response = None
    for guess in guesses:
        if contact == guess[1]:
            print(guess)
       	    response = "Do you want to pay {}{} to {}?".format(amount,currency,guess[1]+' '+guess[0])
    if not response:
        response = "Well you don't have that person in your contact list..."
    return response


def friend_transfer(req):
    """Returns a string containing text with a response to the user
    """
    parameters = req['result']

    response = "Not ready yet"
    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    try:
        response = handle_money(parameters)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error
#    response = "dummy"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

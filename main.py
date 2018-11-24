# -*- coding:utf8 -*-
# !/usr/bin/env python

import json

from flask import Flask, request, make_response, jsonify


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
    res = "Nothig happened"
    try:
        action = req['result']['action']#
#        action = req.get('result').get('action')
    except AttributeError as e:
        print("ERRRROR JSON")
        print(e)
        return 'json error'

    if action == 'transfer.money.yes':
        res = friend_transfer(req)

    r = {'fulfillmentText': res}
    print("WHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT?!")
    print(res)

#    base = {
#                 'speech':"sample response"}

    return jsonify({'speech':res})#, "speech": "this text is spoken out loud if the platform supports voice interactions",
#}) #make_response(jsonify(r))# make_response(r)


def handle_money(params):
    response = "Hi there it worked!"
    return response


def friend_transfer(req):
    """Returns a string containing text with a response to the user
    """
    parameters = req['result']['parameters']

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

"""
Routes and views for the flask application.
"""

from datetime import datetime
from GolfCard import app
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send
from flask_socketio import emit
import random as r 
import json


def log(msg, file = 'log.txt'):
    with open(file, 'w') as logg:
        msg = str(msg)
        logg.write(f'{msg}\n')

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def setNewGame():
    suits = ['spades','hearts','clubs','diamonds']
    cardValues = {'A': 1, '2': -2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'Q': 10,'K': 0,'joker': -2}
    deck = [{'suit':s ,'card':c ,'value':v} for c,v in cardValues.items() for s in suits]
    r.shuffle(deck)
    game = {"deck": deck, 'player' : ['aa','bb','cc']}
    game['hand'] = {x: {'top':[{'hidden': 1, 'card': game['deck'].pop()} for i in range(3)], 'bottom':[{'hidden': 1, 'card': game['deck'].pop()} for i in range(3)] } for x in game['player']}


@socketio.on('getDeck')
def sendDeck():
    print('deck sending now')
    return game

@app.route('/contacts')
def contacts():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/abouts')
def about():
    """Renders the about page."""
    print('about')
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

suits = ['spades','hearts','clubs','diamonds']
cardValues = {'A': 1, '2': -2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'Q': 10,'K': 0,'joker': -2}
deck = [{'suit':s ,'card':c ,'value':v} for c,v in cardValues.items() for s in suits]
r.shuffle(deck)
game = {"deck": deck, 'player' : ['a1','a2','a3']}
game['hand'] = {x: {'top':[{'hidden': 1, 'card': game['deck'].pop()} for i in range(3)], 'bottom':[{'hidden': 1, 'card': game['deck'].pop()} for i in range(3)] } for x in game['player']}







@app.route('/game')
def index():
    j = json.dumps(game)
    print(f'json: {game}\n\n')
    print(f'dictionary: {j}\n\n')
    print('index')
    return render_template('cards.html',g=j)


   







if __name__ == '__main__':
    socketio.run(app)

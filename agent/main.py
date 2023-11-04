import requests
import socketio
import json
from Game import Game

sio = socketio.Client()
game = Game()

@sio.event
def connect():
    print("Connection established")
    sio.emit('newgame', ['lvl0', 5], callback=on_newgame_response)

@sio.event
def disconnect():
    print("Disconnected from server")
    exit(0)

@sio.event
def on_newgame_response(data):
    game.setAgentID(data[0])
    game.setGameID(data[1])
    sio.emit('gamestatus', data[0], callback=on_gamestatus_response)

@sio.event
def on_gamestatus_response(data):
    game.setMap(data)
    game.printValues()
    sio.emit('move', [game.agentID, game.gameID, [1, -1]], callback=on_move_response)
    

@sio.event
def on_move_response(data):
    print('Move response:', data)

@sio.event
def on_lockout_response(data):
    print('Lockout response:', data)

@sio.event
def on_joinagent_response(data):
    print('Join agent response:', data)

if __name__ == '__main__':
    try:
        sio.connect('http://localhost:3000')
        sio.wait()
    except KeyboardInterrupt:
        sio.disconnect()
        exit(0)

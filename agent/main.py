import requests
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connection established")
    sio.emit('newgame', ['lvl0', 5], callback=on_newgame_response)

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.event
def my_response(data):
    print('Received:', data)

@sio.event
def message(data):
    print('Message from server:', data)

@sio.event
def on_newgame_response(data):
    print('New game created:', data)

@sio.event
def on_gamestatus_response(data):
    print('Game status:', data)

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
    sio.connect('http://localhost:3000')
    sio.wait()

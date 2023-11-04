import socketio
import sys
from Game import Game

class Agent:
    def __init__(self):
        self.sio = socketio.Client()
        self.game = Game()
        self.sio.on('connect', self.on_connect)
        self.sio.on('disconnect', self.on_disconnect)
        self.sio.on('newgame_response', self.on_newgame_response)
        self.sio.on('gamestatus_response', self.on_gamestatus_response)
        self.sio.on('move_response', self.on_move_response)
        self.sio.on('lockout_response', self.on_lockout_response)
        self.sio.on('joinagent_response', self.on_joinagent_response)
        self.lvl = input("Enter level (0, 1): ")
        self.iterations = input("Enter number of iterations: ")

    def start(self):
        try:
            self.sio.connect('http://localhost:3000')
            self.sio.wait()
        except (KeyboardInterrupt, SystemExit):
            self.sio.disconnect()
            exit(0)

    def on_connect(self):
        print("Connection established")
        self.sio.emit('newgame', ['lvl' + self.lvl, self.iterations], callback=self.on_newgame_response)

    def on_disconnect(self):
        print("Disconnected from server")

    def on_newgame_response(self, data):
        self.game.setGameID(data[0])
        self.game.setAgentID(data[1])
        self.sio.emit('gamestatus', data[0], callback=self.on_gamestatus_response)

    def on_gamestatus_response(self, data):
        self.game.initMap(data)
        self.firstMaze()

    def moveRight(self):
        self.sio.emit('move', [self.game.gameID, self.game.agentID, "RIGHT"], callback=self.on_move_response)

    def moveLeft(self):
        self.sio.emit('move', [self.game.gameID, self.game.agentID, "LEFT"], callback=self.on_move_response)

    def moveUp(self):
        self.sio.emit('move', [self.game.gameID, self.game.agentID, "UP"], callback=self.on_move_response)

    def moveDown(self):
        self.sio.emit('move', [self.game.gameID, self.game.agentID, "DOWN"], callback=self.on_move_response)

    def updateGame(self, data):
        self.game.setMap(data[0])
        self.game.setScore(data[1])

    def lockout(self):
        self.sio.emit('lockout', [self.game.gameID, self.game.agentID], callback=self.on_lockout_response)

    def firstMaze(self):
        self.moveRight()
        self.moveRight()
        self.lockout()
        self.moveDown()
        self.moveDown()
        self.moveRight()
        self.moveRight()
        self.lockout()
        self.moveDown()
        self.moveDown()
        self.moveLeft()
        self.lockout()
        self.moveLeft()
        self.moveLeft()
        self.moveLeft()
        self.lockout()

    def on_move_response(self, data):
        self.updateGame(data)

    def on_lockout_response(self, data):
        self.game.map.removeValve()
        self.updateGame(data)
        # if self.game.map.nbValves == 0:
        #     print("missing computer", file=sys.stderr)
        if self.game.map.nbValves == -1 and bool(data[2]) == False:
            print("Computer lockouted, resetting map", file=sys.stderr)
            self.game.initMap(data[0])
        elif data[2]:
            print("Computer lockouted, game won and is over with score:", self.game.score)     
            self.sio.disconnect()   
            exit(0)

    def on_joinagent_response(self, data):
        print('Join agent response:', data, file=sys.stderr)
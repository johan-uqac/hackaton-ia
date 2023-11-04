import numpy as np
import ast

class Map:
    def __init__(self) -> None:
        self.map = None
        self.valves = []
        self.nbValves = 0
        self.computer = None
        self.player = None
        
    def setMap(self, mapString):
        baseMap = ast.literal_eval(mapString)
        self.map = np.array(baseMap)
        
    def initMap(self, baseMapString):
        self.setMap(baseMapString)
        print(self.map)
        playerTuple = np.where((self.map == 1) | (self.map == 3) | (self.map == 5) | (self.map == 7))
        self.player = (playerTuple[0][0], playerTuple[1][0])
        valveTuple = np.where((self.map == 2) | (self.map == 3) | (self.map == 6) | (self.map == 7))
        self.valves = [(valveTuple[0][i], valveTuple[1][i]) for i in range(len(valveTuple[0]))]
        self.nbValves = len(self.valves)
        computerTuple = np.where((self.map == 4) | (self.map == 5) | (self.map == 6) | (self.map == 7))
        self.computer = (computerTuple[0][0], computerTuple[1][0])
        
    def getMap(self):
        return self.map

    def getValves(self):
        return self.valves

    def getComputer(self):
        return self.computer
    
    def getPlayer(self):
        return self.player
    
    def removeValve(self):
        self.nbValves -= 1
    
    def printValues(self):
        print("map", self.map)
        print("valves", self.valves)
        print("nbValves", self.nbValves)
        print("computer", self.computer)
        print("player", self.player)
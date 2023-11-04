import numpy as np
import ast

class Map:
    def __init__(self) -> None:
        self.map = None
        self.valves = []
        self.computer = None
        self.player = None
        
    def initMap(self, baseMapString):
        baseMap = ast.literal_eval(baseMapString)
        self.map = np.array(baseMap)
        valveTuple = np.where(self.map == 2)
        self.valves = [(valveTuple[0][i], valveTuple[1][i]) for i in range(len(valveTuple[0]))]
        computerTuple = np.where(self.map == 4)
        self.computer = (computerTuple[0][0], computerTuple[1][0])
        playerTuple = np.where(self.map == 1)
        self.player = (playerTuple[0][0], playerTuple[1][0])
    
    def printValues(self):
        print(self.map)
        print(self.valves)
        print(self.computer)
        
    def getMap(self):
        return self.map

    def getValves(self):
        return self.valves

    def getComputer(self):
        return self.computer
    
    def getPlayer(self):
        return self.player
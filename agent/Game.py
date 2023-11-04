from Map import Map
import ast

class Game:
    def __init__(self) -> None:
        self.map = Map()
        self.agentID = None
        self.gameID = None
        self.score = 0
        
    def initMap(self, baseMapString):
        self.map.initMap(baseMapString)
    
    def setMap(self, baseMapString):
        self.map.setMap(baseMapString)
    
    def setAgentID(self, agentID):
        self.agentID = agentID
    
    def setGameID(self, gameID):
        self.gameID = gameID
        
    def setScore(self, score):
        self.score = score
    
    def printValues(self):
        print("Agent ID:", self.agentID)
        print("Game ID:", self.gameID)
        print("Score:", self.score)
        self.map.printValues()
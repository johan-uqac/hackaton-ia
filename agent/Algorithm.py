from Bfs import BFS
from Node import Node

class Algorithm:
    def __init__(self, gameMap):
        self.binaryTree = Node(gameMap.player, 0)
        self.bfs = BFS(gameMap, self.binaryTree)
        
    def getMoves(self):
        return self.bfs.algo()
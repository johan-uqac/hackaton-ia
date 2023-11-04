from Bfs import BFS

class Algorithm:
    def __init__(self, gameMap):
        self.bfs = BFS(gameMap)
        
    def getMoves(self):
        return self.bfs.algo()
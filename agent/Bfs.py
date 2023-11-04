from collections import deque
import itertools
import numpy as np

class BFS:
    def __init__(self, mapToResolve) -> None:
        self.map = mapToResolve
    
    def distance(self, x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def calcDistance(self, player, valve):
        return self.distance(player[0], player[1], valve[0], valve[1])

    def bfs(self):
        permutations = list(itertools.permutations(self.map.valves))

        best_distance = float('inf')
        best_path = None

        for idx, perm in enumerate(permutations):
            perm_with_computer = list(perm) + [self.map.computer]
            dist = 0
            player = (0, 0)

            for j in perm_with_computer:
                dist += self.distance(player[0], player[1], j[0], j[1])
                player = j
                if dist >= best_distance:
                    break

            if dist < best_distance:
                best_distance = dist
                best_path = perm_with_computer

        return best_path
    
    def calculateMove(self, valve):
        moveList = []
        moveX = valve[0] - self.map.player[0]
        moveY = valve[1] - self.map.player[1]
        for i in range(abs(moveX)):
            if moveX > 0:
                moveList.append("RIGHT")
            else:
                moveList.append("LEFT")
        for i in range(abs(moveY)):
            if moveY > 0:
                moveList.append("DOWN")
            else:
                moveList.append("UP")
        return moveList
    
    def algo(self):
        moves = []
        orderValvePositions = self.bfs()
        # print(orderValvePositions)

        for valvePosition in orderValvePositions:
            # print("valve = ", valvePosition)
            moves.append(self.calculateMove(valvePosition))
            self.map.player = valvePosition
        # print(moves)
        return moves
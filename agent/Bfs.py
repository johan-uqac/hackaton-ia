from collections import deque

class BFS:
    def __init__(self, mapToResolve, binaryTree) -> None:
        self.map = mapToResolve
        self.binaryTree = binaryTree
    
    def distance(self, x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def calcDistance(self, player, valve):
        return self.distance(player[0], player[1], valve[0], valve[1])

    def bfs(self, root):
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            result.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return result
    
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
        print(self.map.valves)
        print(self.map.player)
        print(self.map.computer)
        for valve in self.map.valves:
            self.binaryTree.insertData(valve, self.calcDistance(self.map.player, valve))

        orderValvePositions = self.bfs(self.binaryTree)

        for valvePosition in orderValvePositions:
            moves.append(self.calculateMove(valvePosition))
            self.map.player = valvePosition
        return moves
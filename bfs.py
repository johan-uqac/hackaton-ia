import sys
import os
from collections import deque

# GRID = [
#     [1, 0, 2, 0, 0],
#     [0, 0, 0, 0, 2],
#     [0, 0, 0, 0, 2],
#     [0, 0, 0, 0, 0],
#     [4, 0, 0, 2, 0]
# ]
GRID = [
    [1, 0, 2, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0],
]

class Node:
    def __init__(self, data, distance) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.distance = distance

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print("position", self.data, "distance = ", self.distance)
        if self.right:
            self.right.PrintTree()

    def insertData(self, data, distance):
        # print(data)
        # print("self data = ", self.data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, distance)
                else:
                    self.left.insertData(data, distance)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, distance)
                else:
                    self.right.insertData(data, distance)
        else:
            self.data = data
            self.distance = distance

    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res

    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res

    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def findPlayerPos(grid):
    count, x, y = 0, 0, 0
    for count, x in enumerate(grid):
        for index, y in enumerate(x):
            if y == 1:
                return (count, index)
    return None

def findValvePos(grid):
    valve_pos = []
    count, x, y = 0, 0, 0
    for count, x in enumerate(grid):
        for index, y in enumerate(x):
            if y == 2:
                valve_pos.append((count, index))
    return valve_pos

def calcDistance(player, valve):
    return distance(player[0], player[1], valve[0], valve[1])

def bfs(root):
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

def dijkstra(grid, start, end):
    
    return

def main():    
    player = findPlayerPos(GRID)
    valve = findValvePos(GRID)
    print("player by func = ", player, "valve by func = ", valve)
    root = Node((0, 0), 0)
    for i in valve:
        print("distance from player = ", calcDistance(player, i))
        root.insertData(i, calcDistance(player, i))
    root.PrintTree()
    print(bfs(root))

if __name__ == '__main__':
    main()


# calcul distance entre 2 points
# d = √(x2−x1)2+(y2−y1)2


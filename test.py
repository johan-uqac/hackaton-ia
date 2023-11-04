# import sys
# import os

# game_map = [
#     [1, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 2],
#     [0, 0, 0, 0, 0],
#     [4, 0, 0, 2, 0]
# ],

# # 1 joueur
# # 2 valve
# # 4 machine

# class Node:
#     def __init__(self, data) -> None:
#         self.left = None
#         self.right = None
#         self.data = data

#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()

#     def insertData(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insertData(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insertData(data)
#         else:
#             self.data = data

#     def InOrderTraversal(self, root):
#         res = []
#         if root:
#             res = self.InOrderTraversal(root.left)
#             res.append(root.data)
#             res = res + self.InOrderTraversal(root.right)
#         return res

#     def PreOrderTraversal(self, root):
#         res = []
#         if root:
#             res.append(root.data)
#             res = res + self.PreOrderTraversal(root.left)
#             res = res + self.PreOrderTraversal(root.right)
#         return res

#     def PostOrderTraversal(self, root):
#         res = []
#         if root:
#             res = res + self.PostOrderTraversal(root.left)
#             res = res + self.PostOrderTraversal(root.right)
#             res.append(root.data)
#         return res

# class Game:
#     def __init__(self, player, ia) -> None:
#         self.grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
#         self.player = player
#         self.ia = ia

#     def checkWin(self, player):
#             win = None
#             n = len(self.grid)

#             # checking rows
#             for i in range(n):
#                 win = True
#                 for j in range(n):
#                     if self.grid[i][j] != player:
#                         win = False
#                         break
#                 if win:
#                     return win

#             # checking columns
#             for i in range(n):
#                 win = True
#                 for j in range(n):
#                     if self.grid[j][i] != self.player:
#                         win = False
#                         break
#                 if win:
#                     return win

#             # checking diagonals
#             win = True
#             for i in range(n):
#                 if self.grid[i][i] != player:
#                     win = False
#                     break
#             if win:
#                 return win
#             win = True

#             for i in range(n):
#                 if self.grid[i][n - 1 - i] != player:
#                     win = False
#                     break
#             if win:
#                 return win
#             return False
    
#     def printGrid(self):
#         print('\n'.join(map(lambda x: ' '.join(x), self.grid)))

#     def minimax(self, depth):
        
#         return True

# def main():
#     # game = Game('X', 'O')
#     # root = Node(game.grid)
#     # print(game.checkWin('X'))
#     root = Node(20)
#     root.insertData(14)
#     root.insertData(35)
#     root.insertData(10)
#     root.insertData(19)
#     root.insertData(31)
#     root.insertData(42)
#     root.PrintTree()

#     # [map(lambda val : print(val, sep=""), x)] 
#     # print(list(map(lambda x: ' '.join(x), self.grid)))
# # print("in order", root.InOrderTraversal(root))
# # print("preorder = ", root.PreOrderTraversal(root))
# # print("post order = ", root.PostOrderTraversal(root))
# if __name__ == '__main__':
#     main()


import heapq

def dijkstra_2d(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    shortest_distances = {}
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            shortest_distances[node] = float('infinity')
    shortest_distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        i, j = current_node
        neighbors = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1)
        ]

        for neighbor in neighbors:
            x, y = neighbor
            if 0 <= x < rows and 0 <= y < cols:
                distance = current_distance + grid[x][y]

                if distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances[end]

# Example usage:
grid = [
    [1, 0, 2, 0, 0],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0],
    [4, 0, 0, 2, 0]
]

start_node = (0, 0)
end_node = (0, 2)

shortest_distance = dijkstra_2d(grid, start_node, end_node)
print("Shortest distance from", start_node, "to", end_node, "is:", shortest_distance)

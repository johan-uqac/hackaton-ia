class Node:
    def __init__(self, data, distance) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.distance = distance
        
    def insertData(self, data, distance):
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
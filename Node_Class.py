class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    #Node Insertion
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data> self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    #printing in Inorder
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end = " ")
        if self.right:
            self.right.printTree()
            

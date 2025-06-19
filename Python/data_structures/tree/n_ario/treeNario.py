class Node:
    def __init__(self, data):
        self.data=data
        self.list=[]



class Tree(Node):
    def __init__(self):
        self.root=None

    def createRoot(self, data):
        if (self.root is None):
            print("Add root!")
            self.root= Node(data)
        else:
            self.root= Node(data)
            self.root.list=[]






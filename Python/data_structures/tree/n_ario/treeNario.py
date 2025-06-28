"""
This code implements a simple tree structure in Python, 
allowing for the creation of nodes and a tree, 
adding children to nodes, and displaying the tree structure. 
The `Node` class represents each node in the tree, 
while the `Tree` class manages the overall tree structure. 
The code includes methods to add children and display 
the tree in a hierarchical format.

File: treeNario.py
Author: Anthony Bañon
Created: 2025-06-28
Last Updated: 2025-06-28
"""


class Node:
    def __init__(self, data):
        self.data=data
        self.list=[]

    def addChild(self, children):
        self.list.append(children)



class Tree:
    def __init__(self):
        self.root=None
    
    def haveRoot(self, children):
        if (self.root == None):
            print("Add root first!")
            self.list.append(children)
        else:
            print("root already exist!")
            
           
        
    
    def showTree(self, level=0):
        print(" " * level + str(self.root.data))
        for child in self.root.list:
            child.showTree(level + 1)
        
        
root = Node("Root")

tree = Tree()
tree.addChild(root)

c = Node("C")
d = Node("D")

tree.addChild(c)
tree.addChild(d)

user = Node("User")
programFile = Node("Program File")
games = Node("Games")
data = Node("Data")
metalGeard = Node("Metal Gear")
finalFantasy = Node("Final Fantasy")

tree.addChild(user)
tree.addChild(programFile)
tree.addChild(games)
tree.addChild(data)


tree.showTree()


"""
Description: Implementation of a stack data structure using objects in Python.
 
File: objectStack.py
Author: Anthony Bañon
Created: 2025-10-02
Last Updated: 2025-10-02
"""


class element():
    def __init__(self, data):
        self.data=data



class stack():
    def __init__(self):
        self.list =[]

    def addElement(self, data):
        self.list.append(element(data))

    def removeElement(self):
        if not self.isEmpty():
            return self.list.pop().data
        else:
            return "Stack is empty"

    def isEmpty(self):
        return len(self.list) == 0
    
        
    def size(self):
        return len(self.list)
    
    def display(self):
        for i in range(len(self.list)-1, -1, -1):
            print(self.list[i].data)

    def search(self, data):
        if self.isEmpty():
            return "Stack is empty"
        for i, elem in enumerate(self.list):
            if elem.data == data:
                return f"Found {data} at position {i}"
        return f"{data} not found in stack"



if __name__ == "__main__":
    s = stack()
    s.addElement(1)
    s.addElement(2)
    s.addElement(3)
    s.addElement(4)
    s.addElement(5)
    print("Stack elements are:")
    s.display()
    print("Stack size is:", s.size())
    print("Removing top element:", s.removeElement())
    print("Stack elements after removing top element:")
    s.display()
    print("Is stack empty?", s.isEmpty())
    print("Searching for element 3:", s.search(3))

  
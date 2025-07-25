"""
A simple implementation of a singly linked list in Python.
 
File: nodo.py
Author: Anthony Bañon
Created: 2025-04-24
Last Updated: 2025-04-24
"""



from graphviz import Digraph
import os

class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
   
    def __init__(self):
        self.head = None
        #self.tail = None
        self.size = 0

    def append(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            #self.tail = new_node
        else:
            #self.tail.next = new_node
            #self.tail = new_node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def delete(self, data):
        current = self.head
        before = None

        while current and current.data != data:
            before = current
            current = current.next
        if current is None:
            print("Element not found")
            return False
        if before is None:
            self.head = current.next
        else:
            before.next = current.next
        self.size -= 1
        return True
    
    # def countNode():
    #     current = self.head
    #     count = 0
    #     while current:
    #         count += 1
    #         current = current.next
    #     return print(f"Count of nodes: {count}")

    def search(self, data):
        current = self.head
        while current:
            
            if current.data == data:
                print("Element found") 
                return current
            current = current.next
        print("Element not found")
        return None
        
    

    def update(self,old_data, new_data):
        
        searched = self.search(old_data)
        if searched is not None:
            searched.data = new_data
            print("Element updated")
            return True
        return False
    
    def lineSort(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def draw(self, filename="simpleLinkedList"):
        dot = Digraph(comment='Singly Linked List')

        current = self.head
        count = 0

        while current:
            node_name = f"node{count}"
            dot.node(node_name, str(current.data))

            if current.next:
                dot.edge(f"node{count}", f"node{count+1}")
            
            current = current.next
            count += 1
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_dir, filename)

        dot.render(output_path, format='png', cleanup=True)
        print(f"Diagram saved as {output_path}.png")

        # dot.render(filename, format='png', cleanup=True)
        # print(f"Diagram saved as {filename}.png")

        
               
             
          
      

if __name__ == "__main__":
    simpleList = LinkedList() 
    simpleList.append(4)
    simpleList.append(2)
    simpleList.append(1)
    simpleList.append(3)

    LinkedList.show(simpleList)
    print("Size of the list: ", simpleList.size)

    # simpleList.search(3)
    # old_data = 3
    # new_data = 20
    # simpleList.update(3,20)
    simpleList.lineSort()
    LinkedList.show(simpleList)

    ### editar
    simpleList.update(4, 5)
    LinkedList.show(simpleList)
    simpleList.draw("simpleLinkedList")


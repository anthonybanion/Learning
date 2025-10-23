"""
This is simple circular linked list implementation in Python.
 
File: simpleCircularList.py
Author: Anthony Bañon
Created: 2025-06-05
Last Updated: 2025-06-05
"""

from graphviz import Digraph
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SimpleCircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Circular link to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1

    def show(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")
        print("Size of list:", self.size)

    def delete(self, data):
        if not self.head:
            print("List is empty")
            return False

        current = self.head
        previous = None

        while True:
            if current.data == data:
                if current == self.head:
                    if current.next == self.head:  # Only one node
                        self.head = None
                    else:
                        # Find last node to update its .next
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = current.next
                        tail.next = self.head
                else:
                    previous.next = current.next
                self.size -= 1
                print(f"Element {data} deleted")
                return True

            previous = current
            current = current.next
            if current == self.head:
                break

        print(f"Element {data} not found")
        return False

    def search(self, data):
        if not self.head:
            print("List is empty")
            return None

        current = self.head
        while True:
            if current.data == data:
                print("Element found")
                return current
            current = current.next
            if current == self.head:
                break
        print("Element not found")
        return None

    def update(self, old_data, new_data):
        node = self.search(old_data)
        if node:
            node.data = new_data
            print(f"Element {old_data} updated to {new_data}")
            return True
        return False

    def lineSort(self):
        if not self.head or self.head.next == self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while True:
                next_node = current.next
                if next_node == self.head:
                    break
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next
                if current == self.head:
                    break
        print("List sorted")

    def draw(self, filename="simpleCircularList"):
        dot = Digraph(comment="Simple Circular Linked List", format="png")
        if not self.head:
            dot.node("empty", "Empty List")
        else:
            current = self.head
            index = 0
            node_names = []

            while True:
                node_name = f"node{index}"
                dot.node(node_name, str(current.data))
                node_names.append(node_name)
                current = current.next
                index += 1
                if current == self.head:
                    break

            for i in range(len(node_names)):
                next_index = (i + 1) % len(node_names)
                dot.edge(node_names[i], node_names[next_index])

        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, cleanup=True)
        print(f"Graph saved as {output_path}.png")

if __name__ == "__main__":
    cl = SimpleCircularList()
    cl.append(10)
    cl.append(20)
    cl.append(30)
    cl.append(40)
    cl.append(50)
    cl.append(60)

    cl.draw("simpleCircularList")
    cl.show()

    cl.delete(20)
    cl.show()

    cl.update(30, 35)
    cl.show()

    cl.search(60)

    cl.lineSort()
    cl.show()

    
        
               
             
          
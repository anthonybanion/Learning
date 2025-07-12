"""
Implementation of a double linked list in Python.
 
File: doubleLinkedList.py
Author: Anthony Bañon
Created: 2025-06-11
Last Updated: 2025-06-11
"""

from graphviz import Digraph
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.former = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.former = current
        self.size += 1

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if not current:
            print("Element not found")
            return False
        if current.former:
            current.former.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.former = current.former
        self.size -= 1
        return True

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print("Element found")
                return current
            current = current.next
        print("Element not found")
        return None

    def draw(self, filename="doubleLinkedList"):
        dot = Digraph(comment="Double Linked List")

        current = self.head
        index = 0
        nodes = []

        # Create nodes
        while current:
            node_name = f"node{index}"
            dot.node(node_name, str(current.data))
            nodes.append((node_name, current))
            current = current.next
            index += 1

        # Create bidirectional edges
        for i in range(len(nodes) - 1):
            dot.edge(nodes[i][0], nodes[i + 1][0], constraint='true')
            dot.edge(nodes[i + 1][0], nodes[i][0], constraint='true')

        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, format='png', cleanup=True)
        print(f"Diagram saved as {output_path}.png")

if __name__ == "__main__":
    double_list = LinkedList()
    double_list.append(4)
    double_list.append(2)
    double_list.append(1)
    double_list.append(3)

    print("Initial list:")
    double_list.show()
    print("Size of the list:", double_list.size)

    double_list.draw("doubleLinkedList")

    print("\nDeleting 2 from the list...")
    double_list.delete(2)

    print("List after deletion:")
    double_list.show()
    print("Size of the list:", double_list.size)

    print("\nSearching for element 4...")
    result = double_list.search(4)
    if result:
        print("Next of 4 is:", result.next.data if result.next else "None")


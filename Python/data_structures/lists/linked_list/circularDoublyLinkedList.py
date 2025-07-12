# Circular Doubly Linked List (Non-Recursive and Recursive)
from graphviz import Digraph
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Non-recursive append
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    # Non-recursive show
    def show(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <=> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")
        print("Size:", self.size)

    # Non-recursive delete
    def delete(self, data):
        if not self.head:
            print("List is empty")
            return False

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                self.size -= 1
                print(f"Element {data} deleted")
                return True
            current = current.next
            if current == self.head:
                break

        print(f"Element {data} not found")
        return False

    # Non-recursive search
    def search(self, data):
        if not self.head:
            print("List is empty")
            return None
        current = self.head
        while True:
            if current.data == data:
                print(f"Element found: {current.data}")
                return current
            current = current.next
            if current == self.head:
                break
        print("Element not found")
        return None

    # Non-recursive update
    def update(self, old_data, new_data):
        node = self.search(old_data)
        if node:
            node.data = new_data
            print(f"Element updated from {old_data} to {new_data}")
            return True
        return False

    # Non-recursive bubble sort
    def lineSort(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next != self.head:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    # Non-recursive draw
    def draw(self, filename="circularDoublyList"):
        dot = Digraph(comment="Circular Doubly Linked List", format="png")
        if not self.head:
            dot.node("empty", "Empty List")
        else:
            visited = set()
            current = self.head
            while True:
                node_id = str(id(current))
                dot.node(node_id, str(current.data))
                next_id = str(id(current.next))
                prev_id = str(id(current.prev))
                dot.edge(node_id, next_id, label="next")
                dot.edge(node_id, prev_id, label="prev")
                visited.add(node_id)
                current = current.next
                if current == self.head:
                    break

        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, cleanup=True)
        print(f"Graph saved as {output_path}.png")

if __name__ == "__main__":
    # Example usage
    cdll = CircularDoublyLinkedList()
    cdll.append(10)
    cdll.append(20)
    cdll.append(30)
    cdll.append(40)
    cdll.append(50)
    cdll.append(60)
    cdll.append(70)
    cdll.append(80)
    cdll.show()
    cdll.update(20, 25)
    cdll.show()
    cdll.delete(10)
    cdll.show()
    cdll.search(30)
    cdll.lineSort()
    cdll.show()
    cdll.draw("circularDoublyLinkedList")
"""
Description: Implementation of a queue data structure using objects in Python.
File: queueObject.py
Author: Anthony Bañon
Created: 2025-10-09
Last Updated: 2025-10-16
"""

class Element:
    """Represents a single element in the queue."""
    def __init__(self, data):
        self.data = data

class Queue:
    """Queue implementation using a list and Element objects."""
    def __init__(self):
        self.list = []

    def addElement(self, data):
        """Add an element to the end of the queue."""
        self.list.append(Element(data))
        print(f"Added: {data}")

    def removeElement(self):
        """Remove the element at the front of the queue."""
        if self.isEmpty():
            return "Queue is empty"
        attended = self.list.pop(0)
        return f"Removed: {attended.data}"

    def isEmpty(self):
        """Check if the queue is empty."""
        return len(self.list) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.list)

    def peek(self):
        """Return the element at the front without removing it."""
        if self.isEmpty():
            return "Queue is empty"
        return self.list[0].data

    def display(self):
        """Display all elements in the queue."""
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements:", [elem.data for elem in self.list])


if __name__ == "__main__":
    q = Queue()
    q.addElement(1)
    q.addElement(2)
    q.addElement(3)
    q.addElement(4)
    q.addElement(5)

    q.display()
    print(q.removeElement())
    q.display()
    print(q.removeElement())
    q.display()
    print("Next element in queue:", q.peek())
    print("Queue size:", q.size())

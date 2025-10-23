from graphviz import Digraph
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedListRecursive:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self._append_recursive(self.head, new_node)
        self.size += 1

    def _append_recursive(self, current, new_node):
        if current.next == self.head:
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self._append_recursive(current.next, new_node)

    def show(self):
        if not self.head:
            print("List is empty")
            return
        self._show_recursive(self.head)
        print("(head)")
        print("Size:", self.size)

    def _show_recursive(self, current, start=True):
        print(current.data, end=" <=> ")
        if current.next != self.head:
            self._show_recursive(current.next, False)

    def delete(self, data):
        if not self.head:
            print("List is empty")
            return False
        deleted, self.head = self._delete_recursive(self.head, data)
        if deleted:
            self.size -= 1
            print(f"Element {data} deleted")
            return True
        print(f"Element {data} not found")
        return False

    def _delete_recursive(self, current, data):
        if current.data == data:
            if current.next == current:
                return True, None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True, current.next if current == self.head else self.head
        elif current.next == self.head:
            return False, self.head
        return self._delete_recursive(current.next, data)

    def search(self, data):
        node = self._search_recursive(self.head, data)
        if node:
            print(f"Element found: {node.data}")
        else:
            print("Element not found")
        return node

    def _search_recursive(self, current, data):
        if current.data == data:
            return current
        if current.next == self.head:
            return None
        return self._search_recursive(current.next, data)

    def update(self, old_data, new_data):
        node = self.search(old_data)
        if node:
            node.data = new_data
            print(f"Updated {old_data} to {new_data}")
            return True
        return False

    def lineSort(self):
        if not self.head or self.head.next == self.head:
            return
        self._lineSort_recursive()

    def _lineSort_recursive(self):
        swapped = False
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
        if swapped:
            self._lineSort_recursive()

    def draw(self, filename):
        dot = Digraph(comment="Recursive Circular Doubly Linked List", format="png")
        visited = set()
        self._draw_recursive(self.head, dot, visited)

        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, cleanup=True)
        print(f"Graph saved as {output_path}.png")

    def _draw_recursive(self, current, dot, visited):
        if not current or id(current) in visited:
            return
        visited.add(id(current))

        node_id = str(id(current))
        next_id = str(id(current.next))
        prev_id = str(id(current.prev))
        dot.node(node_id, str(current.data))
        dot.edge(node_id, next_id, label="next")
        dot.edge(node_id, prev_id, label="prev")
        self._draw_recursive(current.next, dot, visited)

if __name__ == "__main__":
    cll = CircularDoublyLinkedListRecursive()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.append(5)
    cll.append(6)
    cll.append(7)
    cll.append(8)
    cll.append(9)
    cll.show()
    cll.delete(2)
    cll.show()
    cll.update(3, 4)
    cll.show()
    cll.lineSort()
    cll.show()
    cll.draw("circularDoublyListRecursive")  # This will create a graph of the list
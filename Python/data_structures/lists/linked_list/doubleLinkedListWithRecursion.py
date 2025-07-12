from graphviz import Digraph
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.former = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self._append_recursive(self.head, new_node)
        self.size += 1

    def _append_recursive(self, current, new_node):
        if current.next is None:
            current.next = new_node
            new_node.former = current
        else:
            self._append_recursive(current.next, new_node)

    def show(self):
        self._show_recursive(self.head)
        print("None")
        print("Size of list:", self.size)

    def _show_recursive(self, current):
        if current is None:
            return
        print(current.data, end=" <-> ")
        self._show_recursive(current.next)

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return False
        return self._delete_recursive(self.head, data)

    def _delete_recursive(self, current, data):
        if current is None:
            print("Element not found")
            return False
        if current.data == data:
            if current.former:
                current.former.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.former = current.former
            self.size -= 1
            print(f"Element {data} deleted")
            return True
        return self._delete_recursive(current.next, data)

    def search(self, data):
        node = self._search_recursive(self.head, data)
        if node:
            print(f"Element found: {node.data}")
            return node
        else:
            print("Element not found")
            return None

    def _search_recursive(self, current, data):
        if current is None:
            return None
        if current.data == data:
            return current
        return self._search_recursive(current.next, data)

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        self._sort_recursive(self.head)

    def _sort_recursive(self, current):
        if current is None or current.next is None:
            return
        next_node = current.next
        self._sort_recursive(next_node)
        if current.data > next_node.data:
            current.data, next_node.data = next_node.data, current.data
            self._sort_recursive(self.head)

    def draw(self, filename="doubleLinkedList"):
        dot = Digraph(comment="Double Linked List", format="png")
        visited = set()
        self._draw_recursive(self.head, dot, visited)

        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, cleanup=True)
        print(f"Graph saved as {output_path}.png")

    def _draw_recursive(self, current, dot, visited):
        if current is None or id(current) in visited:
            return
        visited.add(id(current))

        node_id = str(id(current))
        dot.node(node_id, str(current.data))

        if current.next:
            next_id = str(id(current.next))
            dot.node(next_id, str(current.next.data))
            dot.edge(node_id, next_id, label="next")
            dot.edge(next_id, node_id, label="former")

        self._draw_recursive(current.next, dot, visited)

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.append(50)
    dll.append(60)
    dll.draw("doubleLinkedListRecursive")
    dll.show()

    dll.delete(20)
    dll.show()

    dll.search(30)

    dll.sort()
    dll.show()

    

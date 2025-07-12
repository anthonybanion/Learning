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
            new_node.next = new_node
        else:
            self._append_recursive(self.head, new_node)
        self.size += 1

    def _append_recursive(self, current, new_node):
        if current.next == self.head:
            current.next = new_node
            new_node.next = self.head
        else:
            self._append_recursive(current.next, new_node)

    def show(self):
        if not self.head:
            print("List is empty")
        else:
            self._show_recursive(self.head)
            print("(back to head)")
            print("Size of list:", self.size)

    def _show_recursive(self, current, start=True):
        print(current.data, end=" -> ")
        if current.next != self.head:
            self._show_recursive(current.next, False)

    def delete(self, data):
        if not self.head:
            print("List is empty")
            return False
        deleted, self.head = self._delete_recursive(None, self.head, data)
        if deleted:
            self.size -= 1
            print(f"Element {data} deleted")
            return True
        print(f"Element {data} not found")
        return False

    def _delete_recursive(self, prev, current, data):
        if current.data == data:
            if current.next == current:
                return True, None  # Single-node list
            elif current == self.head:
                tail = self._find_tail_recursive(self.head)
                new_head = current.next
                tail.next = new_head
                return True, new_head
            else:
                prev.next = current.next
                return True, self.head
        elif current.next == self.head:
            return False, self.head
        else:
            return self._delete_recursive(current, current.next, data)

    def _find_tail_recursive(self, node):
        if node.next == self.head:
            return node
        return self._find_tail_recursive(node.next)

    def search(self, data):
        if not self.head:
            print("List is empty")
            return False
        found = self._search_recursive(self.head, data)
        print("Element found" if found else "Element not found")
        return found

    def _search_recursive(self, current, data):
        if current.data == data:
            return True
        if current.next == self.head:
            return False
        return self._search_recursive(current.next, data)
    
    def draw(self, filename="circular_list"):
        dot = Digraph(comment="Simple Circular List", format="png")

        if not self.head:
            dot.node("empty", "Empty List")
        else:
            visited = set()
            self._draw_recursive(self.head, dot, visited)

        # Output path
        output_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        dot.render(output_path, cleanup=True)
        print(f"Graph saved as {output_path}.png")

    def _draw_recursive(self, current, dot, visited):
        node_id = str(id(current))
        if node_id in visited:
            # Cierre del ciclo
            dot.edge(node_id, str(id(self.head)))
            return

        visited.add(node_id)
        dot.node(node_id, str(current.data))
        dot.edge(node_id, str(id(current.next)))
        self._draw_recursive(current.next, dot, visited)


if __name__ == "__main__":
    cl = SimpleCircularList()

    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.append(4)
    cl.append(5)
    cl.append(6)
    cl.append(7)
    cl.append(8)
    cl.append(9)
    cl.draw("simpleCircularListWithRecursion")
    cl.show()  # 1 -> 2 -> 3 -> (back to head)

    cl.search(2)  # Element found
    cl.search(10)  # Element not found

    cl.delete(3)
    cl.show()  # List is empty

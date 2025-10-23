class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
   
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
        else:
            self._append_recursive(current.next, new_node)

    def show(self):
        self._show_recursive(self.head)
        
    def _show_recursive(self, current):
        if current is None:
            print("None")
            return
        print(current.data, end=" -> ")
        self._show_recursive(current.next)
    
    def delete(self, data):
        self.head = self._delete_recursive(self.head, data)
    def _delete_recursive(self, current, data):
        if current is None:
            print("Element not found")
            return None
        if current.data == data:
            self.size -= 1
            return current.next
        current.next = self._delete_recursive(current.next, data)
        return current

    def search(self, data):
        return self._search_recursive(self.head, data)
    
    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        return self._search_recursive(current.next, data)
    
    def update(self, old_data, new_data):
        self.head = self._update_recursive(self.head, old_data, new_data)

    def _update_recursive(self, current, old_data, new_data):
        if current is None:
            print("Element not found")
            return None
        if current.data == old_data:
            current.data = new_data
            return current
        current.next = self._update_recursive(current.next, old_data, new_data)
        return current


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.show()  # Output: 1 -> 2 -> 3 -> None

    ll.delete(2)
    ll.show()  # Output: 1 -> 3 -> None

    print(ll.search(3))  # Output: True
    print(ll.search(2))  # Output: False

    ll.update(3, 4)
    ll.show()  # Output: 1 -> 4 -> None
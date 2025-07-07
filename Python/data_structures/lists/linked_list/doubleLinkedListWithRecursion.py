class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None
        self.former = None

class doubleLinkedList:
   
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
            return True
        return self._delete_recursive(current.next, data)
    
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
            # Swap data
            current.data, next_node.data = next_node.data, current.data
            self._sort_recursive(current)
    
    def search(self, data):
        found_node = self._search_recursive(self.head, data)
        if found_node:
            print("Element found:", found_node.data)
            return found_node
        else:
            print("Element not found")
            return None
    
    def _search_recursive(self, current, data):
        if current is None:
            return None
        if current.data == data:
            return current
        return self._search_recursive(current.next, data)

if __name__ == "__main__":
    dll = doubleLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.show()  # Output: 10 <-> 20 <-> 30 <-> None
    
    dll.delete(20)
    dll.show()  # Output: 10 <-> 30 <-> None
    
    dll.append(25)
    dll.show()  # Output: 10 <-> 30 <-> 25 <-> None
    
    found_node = dll.search(30)  # Output: Element found: 30
    not_found_node = dll.search(40)  # Output: Element not found
    
    dll.sort()
    dll.show()  # Output: 10 <-> 25 <-> 30 <-> None
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
            new_node.next = new_node  # Point to itself
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
            return
        self._show_recursive(self.head)
        print("(back to head)")
    
    def _show_recursive(self, current):
        if current.next == self.head:
            print(current.data, end=" -> ")
            return
        print(current.data, end=" -> ")
        self._show_recursive(current.next)

    def delete(self, data):
        self.head = self._delete_recursive(self.head, data)
    
    def _delete_recursive(self, current, data):
        if not current:
            return None
        if current.data == data:
            if current.next == self.head:
                self.head = None
                return None
            else:
                # Find the last node to update its next pointer
                last = current
                while last.next != current:
                    last = last.next
                last.next = current.next
                if current == self.head:
                    return current.next
                return self.head
        else:
            current.next = self._delete_recursive(current.next, data)
            return current
        
    def search(self, data):
        if not self.head:
            return False
        return self._search_recursive(self.head, data)
    
    def _search_recursive(self, current, data):
        if current.data == data:
            return True
        if current.next == self.head:
            return False
        return self._search_recursive(current.next, data)
    
# Example usage
if __name__ == "__main__":
    cl = SimpleCircularList()
    cl.append(1)
    cl.append(2)
    cl.append(3)
    cl.show()  # Output: 1 -> 2 -> 3 -> (back to head)
    
    print(cl.search(2))  # Output: True
    print(cl.search(4))  # Output: False
    
    cl.delete(2)
    cl.show()  # Output: 1 -> 3 -> (back to head)
    
    cl.delete(1)
    cl.show()  # Output: 3 -> (back to head)
    
    cl.delete(3)
    cl.show()  # Output: List is empty
    
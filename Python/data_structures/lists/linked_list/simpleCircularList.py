"""
This is simple circular linked list implementation in Python.
 
File: simpleCircularList.py
Author: Anthony Bañon
Created: 2025-06-05
Last Updated: 2025-06-05
"""



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
                if previous is None:
                    # Deleting the head node
                    if current.next == self.head:
                        self.head = None
                    else:
                        previous = self.head
                        while previous.next != self.head:
                            previous = previous.next
                        previous.next = current.next
                        self.head = current.next
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

    def update(self,old_data, new_data):
        searched = self.search(old_data)
        if searched is not None:
            searched.data = new_data
            print("Element updated")
            return True
        return False
    
    def lineSort(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while True:
                if current.next == self.head:
                    break
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
                if current == self.head:
                    break
        print("List sorted")
        return True
    

if __name__ == "__main__":
    cl = SimpleCircularList()
    cl.append(10)
    cl.append(20)
    cl.append(30)
    cl.show()  # Output: 10 -> 20 -> 30 -> None
    cl.delete(20)
    cl.show()  # Output: 10 -> 30 -> None
    cl.update(30, 40)
    cl.show()  # Output: 10 -> 40 -> None
    print(cl.search(10))  # Output: Element found
        
               
             
          
class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None
        self.former = None

class LinkedList:
   
    def __init__(self):
        self.head = None
        #self.tail = None
        self.size = 0

    def append(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            #self.tail = new_node
        else:
            #self.tail.next = new_node
            #self.tail = new_node
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
        before = None
        

        while current and current.data != data:
            before = current
            current = current.next
        if current is None:
            print("Element not found")
            return False
        if before is None:
            self.head = current.next
        else:
            before.next = current.next
        self.size -= 1
        return True
    

__main__ = "__main__"
simpleList = LinkedList() 
simpleList.append(4)
simpleList.append(2)
simpleList.append(1)
simpleList.append(3)

LinkedList.show(simpleList)
print("Size of the list: ", simpleList.size)
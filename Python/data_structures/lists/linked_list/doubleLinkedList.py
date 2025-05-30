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

    # def delete(self, data):
    #     current = self.head
    #     before = None      

    #     while current and current.data != data:
    #         before = current
    #         current = current.next
    #     if current is None:
    #         print("Element not found")
    #         return False
    #     if before is None:
    #         self.head = current.next
    #     else:
    #         before.next = current.next
    #         current.former = before
    #     self.size -= 1
    #     return True

    def delete(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if not current:
            print("Element not found")
            return False 
        if not current.former:
                self.head = current.next
        else:
            current.former.next = current.next
            return True  
        if current.next:
            current.next.former = current.former


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print("Element found")
                return current
            current = current.next
        print("Element not found")
        return None




__main__ = "__main__"
doubleList = LinkedList() 
doubleList.append(4)
doubleList.append(2)
doubleList.append(1)
doubleList.append(3)

LinkedList.show(doubleList)
print("Size of the list: ", doubleList.size)

LinkedList.delete(doubleList, 2)
LinkedList.show(doubleList)
print(doubleList.search(4).next)

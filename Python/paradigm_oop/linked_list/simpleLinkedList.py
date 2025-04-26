"""
Description: 
 
File: nodo.py
Author: Anthony Bañon
Created: 2025-04-24
Last Updated: 2025-04-24
"""




class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlasada:
   
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
        self.size += 1

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
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
    
    # def countNode():
    #     current = self.head
    #     count = 0
    #     while current:
    #         count += 1
    #         current = current.next
    #     return print(f"Count of nodes: {count}")

    def search(self, data):
        current = self.head
        while current:
            current = current.next
            if current.data != data:
                print("Element not found") 
                return False
            else:
                print("Element found")
                return True

               
            
          
      

__main__ = "__main__"
simpleList = ListaEnlasada() 
simpleList.append(1)
simpleList.append(2)
simpleList.append(3)
simpleList.append(4)

ListaEnlasada.show(simpleList)
print("Size of the list: ", simpleList.size)
simpleList.delete(2)
ListaEnlasada.show(simpleList)
print("Size of the list: ", simpleList.size)

print("Element found: ", simpleList.search(3))


### editar


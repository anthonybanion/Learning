"""
This code implements a simple binary tree structure in Python
 
File: binaryTree.py
Author: Anthony Bañon
Created: 2025-06-28
Last Updated: 2025-06-28
"""



class BinaryNode:
    def __init__(self, elem:object, node_left:'BinaryNode'=None, node_right: 'BinaryNode'=None)->None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    
    # def __eq__(self, other: 'BinaryNode')->bool:
    #     return other is not None and self.elem == other.elem and \
    #         self.left == other.left and self.right == other.right
            
class BinaryTree:
    def __init__(self)->None:     
        self._root = None
    
    def __eq__(self, other: 'BinaryTree')->bool:
        return other is not None and self._root == other._root
    
    def size(self)->int:
        """Returns the number of nodes in the tree."""
        return self._size(self._root)
        
    def _size(self, node: BinaryNode)->int:
        """Helper method to calculate the size of the tree."""
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
    
    def height(self)->int:
        return self._height(self._root)
    
    def _height(self, node: BinaryNode)->int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def preorder(self)->None:
        print('Preorder traversal: ', end=' ')
        self._preorder(self._root)
        print()
    
    def _preorder(self, node:BinaryNode)->None:
        if node is not None:
            print(node.elem, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)
    
if __name__ == "__main__":
    # Example usage
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    root.right = BinaryNode(3)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)

    tree = BinaryTree()
    tree._root = root

    print("Size of the tree:", tree.size())
    print("Height of the tree:", tree.height())
    tree.preorder()
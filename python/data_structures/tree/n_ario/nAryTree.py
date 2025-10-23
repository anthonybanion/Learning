"""
This module implements an N-ary tree 
with basic operations such as size, height, and traversal.

File: newTree.py
Author: Anthony Bañon
Created: 2025-06-28
Last Updated: 2025-06-28
"""


class NaryNode:
    def __init__(self, elem: object):
        self.elem = elem
        self.children = []  # List of child nodes

    def __eq__(self, other: 'NaryNode') -> bool:
        return (
            other is not None and
            self.elem == other.elem and
            self.children == other.children
        )


class NaryTree:
    def __init__(self) -> None:
        self._root = None

    def __eq__(self, other: 'NaryTree') -> bool:
        return other is not None and self._root == other._root

    def size(self) -> int:
        return self._size(self._root)

    def _size(self, node: NaryNode) -> int:
        if node is None:
            return 0
        return 1 + sum(self._size(child) for child in node.children)

    def height(self) -> int:
        return self._height(self._root)

    def _height(self, node: NaryNode) -> int:
        if node is None:
            return -1
        if not node.children:
            return 0
        return 1 + max(self._height(child) for child in node.children)

    def preorder(self) -> None:
        print("Preorder traversal:", end=' ')
        self._preorder(self._root)
        print()

    def _preorder(self, node: NaryNode) -> None:
        if node is not None:
            print(node.elem, end=' ')
            for child in node.children:
                self._preorder(child)

    def find(self, elem: object) -> NaryNode:
        """Find a node with the given element."""
        return self._find(self._root, elem)

    def _find(self, node: NaryNode, elem: object) -> NaryNode:
        if node is None:
            return None
        if node.elem == elem:
            return node
        for child in node.children:
            found = self._find(child, elem)
            if found:
                return found
        return None

    def add(self, parent_elem: object, new_elem: object) -> bool:
        """Add a new node under the node with parent_elem."""
        parent = self.find(parent_elem)
        if parent:
            new_node = NaryNode(new_elem)
            parent.children.append(new_node)
            return True
        return False

    def update(self, old_elem: object, new_elem: object) -> bool:
        """Update the value of a node."""
        node = self.find(old_elem)
        if node:
            node.elem = new_elem
            return True
        return False

    def delete(self, elem: object) -> bool:
        """Delete a node with the given element (and all its subtree)."""
        if self._root is None:
            return False
        if self._root.elem == elem:
            self._root = None
            return True
        return self._delete(self._root, elem)

    def _delete(self, parent: NaryNode, elem: object) -> bool:
        for i, child in enumerate(parent.children):
            if child.elem == elem:
                del parent.children[i]
                return True
            if self._delete(child, elem):
                return True
        return False

if __name__ == "__main__":
    # Example usage
    root = NaryNode(1)
    child1 = NaryNode(2)
    child2 = NaryNode(3)
    child1.children.append(NaryNode(4))
    child1.children.append(NaryNode(5))
    root.children.append(child1)
    root.children.append(child2)

    tree = NaryTree()
    tree._root = root

    print("Size of the tree:", tree.size())
    print("Height of the tree:", tree.height())
    tree.preorder()

    print("Finding node with element 3:", tree.find(3).elem if tree.find(3) else "Not found")
    print("Adding node 6 under node 2:", tree.add(2, 6))
    tree.preorder()
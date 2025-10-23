"""
This code implements a simple tree structure in Python
 
File: tree.py
Author: Anthony Bañon
Created: 2025-06-28
Last Updated: 2025-06-28
"""



class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, target_data):
        self.children = [child for child in self.children if child.data != target_data]
        for child in self.children:
            child.remove_child(target_data)

    def search(self, target_data):
        if self.data == target_data:
            return self
        for child in self.children:
            result = child.search(target_data)
            if result:
                return result
        return None

    def display(self, level=0):
        print("  " * level + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

    def list_all(self):
        nodes = [self.data]
        for child in self.children:
            nodes.extend(child.list_all())
        return nodes


class Tree:
    def __init__(self, root_data=None):
        if root_data is not None:
            self.root = Node(root_data)
        else:
            self.root = None

    def set_root(self, data):
        self.root = Node(data)

    def add_child(self, parent_data, child_data):
        if not self.root:
            print("Tree is empty. Set the root first.")
            return
        parent_node = self.root.search(parent_data)
        if parent_node:
            parent_node.add_child(Node(child_data))
        else:
            print(f"Parent node '{parent_data}' not found.")

    def remove_node(self, target_data):
        if self.root:
            if self.root.data == target_data:
                self.root = None
            else:
                self.root.remove_child(target_data)

    def display(self):
        if self.root:
            self.root.display()
        else:
            print("Tree is empty.")

    def search(self, data):
        if self.root:
            return self.root.search(data)
        return None

    def list_all_nodes(self):
        if self.root:
            return self.root.list_all()
        return []

# Example usage:
if __name__ == "__main__":
    tree = Tree("Root")
    tree.add_child("Root", "Child1")
    tree.add_child("Root", "Child2")
    tree.add_child("Child1", "Grandchild1")
    tree.add_child("Child1", "Grandchild2")

    print("Tree structure:")
    tree.display()

    print("\nAll nodes:")
    print(tree.list_all_nodes())

    print("\nSearching for 'Grandchild2':")
    result = tree.search("Grandchild2")
    if result:
        print("Found:", result.data)
    else:
        print("Not found.")

    print("\nRemoving 'Child1':")
    tree.remove_node("Child1")
    tree.display()

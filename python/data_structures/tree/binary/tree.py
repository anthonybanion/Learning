import graphviz 
from collections import deque  # ✅ Needed for BFS (level order insertion)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        """
        Adds a node to the tree level by level (like a complete binary tree).
        Fills left to right at each level.
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        # BFS to find the first available spot
        queue = [self.root]  # we start from the root
        while queue:
            current = queue.pop(0)  # we take the first node in the queue

            if current.left is None:   # if there is space on the left, we fill it
                current.left = new_node
                return
            else:
                queue.append(current.left)   # If it's busy, we add it to the queue for later review

            if current.right is None:   # if there is space on the right, we fill it
                current.right = new_node
                return
            else:
                queue.append(current.right)   # if it's busy, we also queue it

    def complete_level(self):
        """
        Completes the tree to the last full level.
        ✅ Left unchanged (still fills None nodes).
        """
        if self.root is None:
            return
        self._complete_level(self.root)

    def _complete_level(self, node):
        """Recursively completes the tree to the last full level"""
        if node.left is None and node.right is None:
            node.left = Node(None)
            node.right = Node(None)
        if node.left:
            self._complete_level(node.left)
        if node.right:
            self._complete_level(node.right)

    def print_tree(self, node=None, level=0, prefix="root: "):
        """Prints the tree recursively"""
        if node is None:
            node = self.root
        print(" " * level + prefix + str(node.data))
        if node.left:
            self.print_tree(node.left, level + 2, "left → ")
        if node.right:
            self.print_tree(node.right, level + 2, "right → ")

    def draw_tree(self):
        """Draws the binary tree using Graphviz"""
        dot = graphviz.Digraph(comment="Binary Tree")
        self._draw_tree(self.root, dot)
        dot.render("binary_tree", format="png", view=True)  # generates and opens PNG

    def _draw_tree(self, node, dot):
        if node is not None:
            dot.node(str(node.data), str(node.data))  # create node

            if node.left is not None:
                dot.edge(str(node.data), str(node.left.data))
                self._draw_tree(node.left, dot)

            if node.right is not None:
                dot.edge(str(node.data), str(node.right.data))
                self._draw_tree(node.right, dot)


if __name__ == "__main__":
    # Example usage
    tree = Tree()

    for i in range(36):  # add 0 to 35
        tree.add(i)

    tree.print_tree()
    tree.draw_tree()

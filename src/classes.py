ROOT = 'root' # Constant to store the 'root' value

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None # <- Remember that the binary tree model requires the developer to implement
        self.right = None # two pieces of data in cascade sequence

    def __str__(self): # Returns the given data as a string to avoid type compatibility issues
        return str(self.data)


class BinaryTree:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node # <- Build a subtree starting from a given node
        elif data:
            node = Node(data) # <- Initialize root from raw data
            self.root = node
        else:
            self.root = None # <- Default to empty root

    # performs an symmetric traversal, processing one item on each side at a time
    def symmetric_traversal(self, node=ROOT):
        if node == ROOT: # If the node is empty, traverse starting from the root
            node = self.root

        if node.left: 
            self.symmetric_traversal(node.left) # Displays the items always starting from the left if an item exists at the position

        print(node)

        if node.right:
            self.symmetric_traversal(node.right) # Displays the next item on the right

    
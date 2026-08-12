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

    def symmetric_traversal(self, node=ROOT):
        """ Performs a symmetric (in-order) traversal, processing the left subtree, 
        then the current node, and finally the right subtree. """

        if node == ROOT: # # If the node is the default ROOT sentinel, start from the actual root
            node = self.root

        if node.left: 
            self.symmetric_traversal(node.left) # Recursively traverse the left subtree

        print(node) # Display/process the current central node

        if node.right:
            self.symmetric_traversal(node.right) # Recursively traverse the right subtree

    def postorder_traversal(self, node=ROOT):
        """ Performs a post-order traversal, processing all items of the left subtree, 
        then all items of the right subtree, and finally the current node, 
        which in this case would finally be the root node. """

        if node == ROOT:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left) # Traverse the left subtree first

        if node.right:
            self.postorder_traversal(node.right) # Traverse the right subtree second

        print(node) # Process the current node after both subtrees are done

    
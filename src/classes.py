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
        """ performs an symmetric traversal, processing 
        one item on each side at a time """

        if node == ROOT: # If the node is empty, traverse starting from the root
            node = self.root

        if node.left: 
            self.symmetric_traversal(node.left) # Displays the items always starting from the left if an item exists at the position

        print(node)

        if node.right:
            self.symmetric_traversal(node.right) # Displays the next item on the right

    def postorder_traversal(self, node=ROOT):
        """ performs an post-order traversal, processing all items of left subtree, 
        all items of right subtree and finally, processes the central node, which in this case is the root."""

        if node == ROOT:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left) # Continues traversing to the left until there are no more left nodes

        if node.right:
            self.postorder_traversal(node.right) # Goes to the right after all left nodes have been returned

        print(node) # Displays the current node; once all left and right subtrees are gone, it returns the root

    
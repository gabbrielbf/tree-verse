from queue import Queue

ROOT = 'root' # "Constant" to store the 'root' value

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

    def levelorder_traversal(self, node=ROOT):
        """ Performs a level-order traversal, processing all items level by level from 
        top to bottom and from left to right, visiting all nodes present at the same 
        depth before proceeding to the next level. """

        if node == ROOT:
            node = self.root

        # We use a queue because of its FIFO (First In, First Out) property. 
        # This ensures nodes are processed in the exact order they are 
        # discovered—level by level, from top to bottom and left to right.
        queue = Queue()
        queue.push(node)

        while len(queue): # While the queue size is greater than zero

            node = queue.pop() # Remove and get the next node from the queue

            if node.left: # Add the left child to the queue if it exists
                queue.push(node.left)

            if node.right: # Add the right child to the queue if it exists
                queue.push(node.right)

            print(node, end=' ')

    def preorder_traversal(self, node=ROOT):
        """ Performs a pre-order traversal, processing the root node first, followed by 
        the left subtree and then the right subtree. Unlike post-order where the root comes 
        last, here the root is always the immediate starting point """

        if node == ROOT: 
            node = self.root

        print(node) # Displays the current node, which is currently the ROOT

        if node.left: # Moves to the left subtree
            self.preorder_traversal(node.left)

        if node.right: # Moves to the right subtree after all left children have been visited
            self.preorder_traversal(node.right)

    def height(self, node=ROOT):
        """ Calculates the height of a tree based on the 
        data present in a given node (if one exists) """

        if node == ROOT:
            node = self.root

        height_left = 0 # { Values start at zero because in the conditions below we check IF the node value has an element;
        height_right = 0 # } if it does, we perform the calculation, otherwise the value remains zero

        if node.left:
            height_left = self.height(node.left)

        if node.right:
            height_right = self.height(node.right)

        # Calculating the height of the blocks
        if height_right > height_left:
            return height_right + 1
        else:
            return height_left + 1

    def count_nodes(self, node=ROOT):
        """ Counts the total number of nodes present in the tree
        starting from a given node or the root """

        if node == ROOT: 
            node = self.root

        if node is None: # If the node is empty or null, return zero nodes
            return 0

        count_left = 0 
        count_right = 0 

        if node.left: # If a left child exists, recursively count nodes in the left subtree
            count_left = self.count_nodes(node.left)

        if node.right: # Count nodes in the right subtree, if there are children
            count_right = self.count_nodes(node.right)

        return count_left + count_right + 1 # Sum the nodes from both subtrees and add one for the current node

    def count_leaves(self, node=ROOT):
        """ Counts the total number of leaf nodes (nodes with no children)
        starting from a given node or the root """

        if node == ROOT: 
            node = self.root

        if node is None: # If the node is empty or null, return zero leaves
            return 0

        if node.left is None and node.right is None: # Check if the current node has no children, making it a leaf
            return 1 # Return one because this current node is a leaf

        leaves_left = 0 
        leaves_right = 0 

        if node.left: 
            leaves_left = self.count_leaves(node.left)

        if node.right: 
            leaves_right = self.count_leaves(node.right)

        return leaves_left + leaves_right # Return the total sum of leaves found in both subtrees


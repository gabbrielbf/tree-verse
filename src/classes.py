from queue import Queue

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

        if node.right: # Count nodes in the right subtree
            count_right = self.count_nodes(node.right)

        return count_left + count_right + 1 # Sum the nodes from both subtrees and add one for the current node

class BinarySearchTree(BinaryTree):

    def insert(self, value):
        """ Method responsible for inserting an element 
        into a specific node at a given position in the tree """

        parent = None # Variable created to check the value size
                        # Ex.
        x = self.root   # We test if x is greater than y; if so, we place x to the right,
                        # otherwise it will be allocated to the left.
        while (x): # While this root value is not empty (not null)

            parent = x # We define the parent based on the current value present at the root

            if value < x.data:
                x = x.left # And then we will advance this parent value in a direction
            else:          # defined according to its size compared to the value of the data in the node
                x.right

        if parent is None: # This creates a root with the parameter value
            self.root = Node(value) # to become the root of the tree only IF the CURRENT root is empty
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):
        """ Responsible for searching for a given value within the tree starting from the root. 
        If the user enters a value in the parameter, this value becomes the current root and the 
        search will start from this new "subtree" """

        if node == 0: # If the passed value was not found to
            node = self.root # start the search for it, we begin searching from the root

        if node is None or node.data == value: # If the node is empty or the node equals the value we are looking for in the binary tree, 
             return BinarySearchTree(node)     # we return a search on the subtree starting from that specific node. It doesn't make sense 
                                               # to return the node itself because that would only be valid if we were working with lists; 
                                               # since that is not the case, we can return a subtree starting from that specific node, 
                                               # so as not to make the structure obsolete

        if value < node.data: # In this other case, we check if the value is less than the current node,
            return self.search(value, node.left) # going down to the left because the value is smaller than the current node.
        else:
            return self.search(value, node.right) # Inverse operation.

    def search_min(self, node=ROOT):
        """ We know that as a rule, the smallest value will always be 
        to the left of the tree, so we search through all the left nodes 
        until we find it and then return the stored data """

        if node == ROOT:
            node = self.root

        while node.left: # While there is a left node, search to the left
            node = node.left # until finding and returning the smallest value
        return node.data

    def search_max(self, node=ROOT):
        """ The search logic for the maximum is the same as for the minimum, 
        with the difference that it now goes to the right """

        if node == ROOT:
            node = self.root

        while node.right:
            node = node.right
        return node.data

    
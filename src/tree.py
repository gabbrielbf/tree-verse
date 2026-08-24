from .classes import BinaryTree, Node, ROOT

class BinarySearchTree(BinaryTree):

    def insert(self, value):
        """ Method responsible for inserting an element 
        into a specific node at a given position in the tree """

        parent = None # Variable created to check the value size
                        # Ex.
        current = self.root   # We test if x is greater than y; if so, we place x to the right,
                        # otherwise it will be allocated to the left.
        while (current): # While this root value is not empty (not null)

            parent = current # We define the parent based on the current value present at the root

            if value < current.data:
                current = current.left # And then we will advance this parent value in a direction
            else:          # defined according to its size compared to the value of the data in the node
                current = current.right

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

        if node is None: 
            TEXT = '[Empty tree]'
            return TEXT

        while node.left: # While there is a left node, search to the left
            node = node.left # until finding and returning the smallest value
        return node.data

    def search_max(self, node=ROOT):
        """ The search logic for the maximum is the same as for the minimum, 
        with the difference that it now goes to the right """

        if node == ROOT:
            node = self.root

        if node is None: 
            TEXT = '[Empty tree]'
            return TEXT

        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        """ Method responsible for removing a specific node passed as a parameter; 
        if none is passed, the sentinel root of the tree will be removed, and thus the 
        logic for finding the successor will be applied """
    
        if node == ROOT:
            node = self.root

        if node is None:
            return node

        if value < node.data: # Check if the target value is smaller than current node data
            node.left = self.remove(value, node.left) # Recursively search and remove in the left subtree
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else: # Executed when the target node to delete is found

            if node.left is None: # Check if the node has no left child
                return node.right # Return the right child to replace the current node
            elif node.right is None:
                return node.left
            else: # Executed when the node has both left and right children
                substitute = self.search_min(node.right) # Find the minimum value in the right subtree (in-order successor)
                node.data = substitute # Replace the current node's data with the successor's data
                node.right = self.remove(substitute, node.right) # Recursively remove the duplicate successor node from the right subtree

            return node # Return the updated node reference to maintain tree structure


class AVLTree(BinarySearchTree):
    pass



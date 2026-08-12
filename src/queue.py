# Supporting data structure (made by me) to be used in the 
# level-order traversal method of the file (classes.py)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0 # Keeps track of the number of elements in the queue

    def push(self, elem):
        """ Inserts an element at the end of the queue. """

        node = Node(elem) 
        
        if self.last is None: # If the queue is empty, the new node is both first and last
            self.last = node
        else: # Link the current last node to the new node, then update self.last
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        """ Removes and returns the element from the front of the queue. """

        if self._size > 0:
            elem = self.first.data # Retrieve data from the front node
            self.first = self.first.next

            if self.first is None:
                self.last = None

            # Decrement the size and return the retrieved element
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        """ Returns the element at the front of the queue without removing it. """

        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        """ Returns the size of the queue. """
        return self._size

    def __repr__(self):

        if self._size > 0:
            r = ""
            pointer = self.first

            # Traverse through all nodes and append their data to the string
            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        
        return "Empty Queue"

    def __str__(self):
        """ Returns the string representation when printing the queue. """
        return self.__repr__()
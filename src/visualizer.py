from menu import traversals
import time, sys
from graphviz import Digraph # <- importing "Digraph" to replace the logic of displaying nodes in the terminal

class Visualizer:

    def __init__(self, bst):
        self.bst = bst # Stores the received tree so that all methods can access it
    
    def _write(self, text, delay=0.04):
        """ Writes node by node dynamically """

        for char in str(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

    def _get_levels(self):
        """ Organizes the tree nodes by level """

        if self.bst.root is None:
            return []

        # Creates the first level containing the root
        levels = [[(self.bst.root, 0)]] # The second value (0) represents the position of the node within that level
        current = levels[0] # <- Starts processing from the first level of the tree

        while current: # While there is a level to process

            next_level = []

            for node, position in current: # <- Traverses each node of the current level along with its position
                if node.left: # Checks if the current node has a left child
                    next_level.append((node.left, position * 2)) # <- The left child receives a position based on the parent's position

                if node.right:
                    next_level.append((node.right, position * 2 + 1))

            if not next_level: # <- If there are no more children, it means we have reached the last level
                break

            levels.append(next_level) # Adds the next level to the general list
            current = next_level # The next level becomes the current level

        return levels # Returns all found levels

    def _get_position(self, position, level, height, spacing):
        """ Calculates the horizontal position of a node """

        # Calculates how many spaces/positions exist in that level
        slots = 2 ** level
        distance = spacing * (2 ** (height - level - 1)) # <- Calculates the horizontal distance between the nodes of that level

        return (position * distance) + (distance // 2) # Returns the center position where the node should be drawn

    def display_tree(self):
        """ Displays the tree in a hierarchical format """

        if self.bst.root is None:
            self._write('\n[Empty tree]\n')
            return

        levels = self._get_levels() # Gets all tree levels.
        height = len(levels) # The amount of levels represents the visual height of the tree

        # Searches for the largest value size existing in the tree,
        # this helps to define an appropriate minimum spacing
        largest_value = max(
            len(str(node.data)) # Counts how many characters the node value has
            for level in levels  # Traverses each tree level
            for node, _ in level  # Traverses each node of that level
        )

        spacing = max(6, largest_value + 4) # Defines the minimum space between nodes
                                            # The value 6 prevents simple trees from getting too cramped

        width = (2 ** (height - 1)) * spacing # Defines the total available width to draw the tree,
                                        # the greater the height, the greater the required space

        for level_index, level in enumerate(levels): # <- Traverses each tree level starting from the root

            # Creates an empty line represented by spaces,
            # and it is on this line that the node values will be positioned
            line = [' '] * width

            for node, position in level: # <- Traverses all existing nodes in that level

                # Calculates exactly where this node's value should appear horizontally
                x = self._get_position(
                    position,     # Logical position of the node within the level
                    level_index,  # Current level
                    height,       # Total height of the tree
                    spacing       # Previously defined spacing
                )

                value = str(node.data)

                # Calculates where the first character of the value should start
                # The goal is to center the value at the calculated position
                start = x - len(value) // 2

                for index, char in enumerate(value): # <- Traverses each character of the node's value.
                    if 0 <= start + index < width: # <- Checks if the calculated position is within the line width.
                        # Puts the character in the correct position of the line
                        line[start + index] = char

            # Joins all spaces and characters of the line into a single string,
            # rstrip() removes unnecessary spaces at the end and
            # '\n' jumps to the next terminal line
            self._write(''.join(line).rstrip() + '\n')

            # Logic for the connection between nodes:
            if level_index == height - 1: # <- If this is the last level, there are no children to connect
                continue

            # Gets the level that will be connected to the current level
            next_level = levels[level_index + 1]

            # Creates a new empty line to draw the branches
            connections = [' '] * width

            for node, position in level: # <- Traverses the nodes of the current level to find their children

                # Calculates the horizontal position of the parent node
                parent_x = self._get_position(
                    position,
                    level_index,
                    height,
                    spacing
                )

                if node.left: # <- Checks if the node has a left child

                    # Calculates the horizontal position of the left child
                    child_x = self._get_position(
                        position * 2,
                        level_index + 1,
                        height,
                        spacing
                    )

                    # Finds the midpoint between parent and child and
                    # it is at this point that we will place the '/' character
                    x = (parent_x + child_x) // 2

                    if 0 <= x < width: # <- Ensures the position is within the line and then draws the left branch
                        connections[x] = '/'

                if node.right: # <- Checks if the node has a right child

                    # Calculates the horizontal position of the right child
                    child_x = self._get_position(
                        position * 2 + 1,
                        level_index + 1,
                        height,
                        spacing
                    )

                    x = (parent_x + child_x) // 2

                    if 0 <= x < width:
                        connections[x] = '\\'

            # Joins the characters of the branch line and displays it in the terminal
            self._write(''.join(connections).rstrip() + '\n')

    # Traversals below will use the logic developed by the "display_tree" method above and elaborate their own displays according
    # to their respective display characteristic:
    def _symmetric(self, node): # <- Only continues if the node exists
        if node:
            # First traverses the entire left part
            yield from self._symmetric(node.left)
            # Then returns the current node's value
            yield node.data
            # Finally traverses the entire right part
            yield from self._symmetric(node.right)

    def _preorder(self, node):
        if node:
            yield node.data
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.data

    def _levelorder(self):
        """ Level-order traversal: top to bottom and left to right """

        if self.bst.root is None:      
            return

        # Creates a queue starting from the root
        queue = [self.bst.root]

        while queue: # <- While there are nodes in the queue

            node = queue.pop(0) # Removes the first node from the queue

            # Returns the value of this node
            yield node.data

            if node.left:   
                queue.append(node.left)  

            if node.right:
                queue.append(node.right)

    def _display_traversal(self, title, values):
        """ Displays the tree itself, method to be used by the traversals below """

        if self.bst.root is None:
            return

        self._write(f'\n{title}\n')

        self._write('=' * len(title) + '\n')

        # Traverses the values produced by the traversal algorithm
        for value in values:

            # Displays each value with a small animation
            self._write(f'{value} ', 0.04)
            time.sleep(0.2)
        self._write('\n')

        self._write('=' * len(title) + '\n')

    def display_symmetric(self):
        """ Displays the tree and then the symmetric traversal """

        self.display_tree() # First visually draws the tree

        # Executes the symmetric traversal and sends its values to the display
        self._display_traversal(
            'Symmetric Traversal ⤵️ :',
            self._symmetric(self.bst.root)
        )

    def display_preorder(self):
        """ Displays the tree and then the pre-order traversal """

        self.display_tree()

        self._display_traversal(
            'Pre-Order Traversal ⤵️ :',
            self._preorder(self.bst.root)
        )

    def display_postorder(self):
        """ Displays the tree and then the post-order traversal """

        self.display_tree()            

        self._display_traversal(
            'Post-Order Traversal ⤵️ :',
            self._postorder(self.bst.root)
        )

    def display_level(self):
        """ Displays the tree and then the level-order traversal """

        self.display_tree()

        self._display_traversal(
            'Level-Order Traversal ⤵️ :',
            self._levelorder()
        )

    
def wich_traversal(bst):
    """ Function that will dynamically display each traversal 
    of its respective property in the terminal to the 
    user according to a return from "traversals """

    visualizer = Visualizer(bst)

    match traversals():
        case 1:
            visualizer.display_tree()
        case 2:
            visualizer.display_symmetric()
        case 3:
            visualizer.display_postorder()
        case 4:
            visualizer.display_level()
        case 5:
            visualizer.display_preorder()


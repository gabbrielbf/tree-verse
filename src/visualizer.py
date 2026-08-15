from menu import traversals
import time, sys

class Visualizer:

    def __init__(self, bst):
        self.bst = bst
    
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

        levels = [[(self.bst.root, 0)]]
        current = levels[0]

        while current:
            next_level = []

            for node, position in current:
                
                if node.left:
                    next_level.append((node.left, position * 2))

                if node.right:
                    next_level.append((node.right, position * 2 + 1))

            if not next_level:
                break

            levels.append(next_level)
            current = next_level

        return levels


def wich_traversal(bst):

    visualizer = Visualizer(bst)

    match traversals():
        case 1:
            pass

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass


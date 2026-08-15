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

    def _get_position(self, position, level, height, spacing):
        """ Calculates the horizontal position of a node """

        slots = 2 ** level
        distance = spacing * (2 ** (height - level - 1))

        return ((position * distance) + distance) // 2

    def display_tree(self):
        """ Displays the tree in a hierarchical format """

        if self.bst.root is None:
            self._write('[Empty tree]\n')
            return

        levels = self._get_levels()
        height = len(levels)

        # Espaço mínimo entre dois nós.
        largest_value = max(
            len(str(node.data))
            for level in levels
            for node, _ in level
        )

        spacing = max(6, largest_value + 4)
        width = (2 ** height) * spacing

        

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


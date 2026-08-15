from menu import traversals
import time, sys

class Visualizer:

    def __init__(self, bst):
        self.bst = bst

    def _write(self, text, delay=0.04):
        
        for char in str(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


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


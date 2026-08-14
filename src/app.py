from tree import BinarySearchTree
from menu import numbered_menu, clear_terminal, read_numeric_option
from visualizer import wich_traversal

bst = BinarySearchTree()

def run_code():

    while True:

        clear_terminal()
        match numbered_menu():

            case 1:
                try:
                    value = int(input('Which value to insert -> '))
                    bst.insert(value)
                    print(f'Value [{value}] successfully inserted ✅\n')
                except ValueError:
                    print('[ERROR] Invalid value!\n')
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass

run_code()
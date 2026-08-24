from .tree import BinarySearchTree
from .menu import numbered_menu, clear_terminal, exit_program, teach_user
from .visualizer import wich_traversal
from .utils import tip

bst = BinarySearchTree()

teach_user()
clear_terminal()
tip()

def run_code():

    while True:

        clear_terminal()
        match numbered_menu():

            case 1:
                while True:
                    try:
                        value = int(input('Which value to insert -> '))
                        bst.insert(value)
                        print(f'Value [{value}] successfully inserted ✅')
                    except ValueError:
                        print('\n[ERROR] Invalid value!\n')
                        continue
                    break
            case 2:
                while True:
                    try:
                        choice = str(input('Do you want to search from a specific value? [Y/N]: ')).strip().upper()

                        if choice == 'Y': # If the user decides to search for a specific value, this value becomes the new root/subtree
                            value = int(input('Enter the value to become the new root/subtree -> '))

                            subtree = bst.search(value)

                            if (subtree is None or
                                subtree.root is None):
                                print(f'\n[ERROR] Value [{value}] does not exist in the tree!\n')
                                continue

                            print(f'\n[SUB-TREE MAX. Value]: {subtree.search_max()}') # Displaying largest and smallest values
                            print(f'[SUB-TREE MIN. Value]: {subtree.search_min()}') # Starting from this new sub-tree
                        else:
                            print(f'\n[TREE MAX. Value]: {bst.search_max()}')
                            print(f'[TREE MIN. Value]: {bst.search_min()}')
                    except ValueError:
                        print('\n[ERROR] Invalid value!')
                        continue
                    break
            case 3:
                while True:
                    try:
                        value = int(input('Which value to remove -> '))

                        subtree = bst.search(value) # Using search to know if the value exists in the tree
                        if (subtree is None or # If the node value is empty or if the tree itself is empty
                            subtree.root is None):
                            print(f'\n[ERROR] Value [{value}] does not exist in the tree!')
                            break

                        bst.root = bst.remove(value) # If it is not, perform the operation
                        print(f'Value [{value}] successfully removed ❌')
                    except ValueError:
                        print('\n[ERROR] Invalid value!\n')
                        continue
                    break
            case 4:
                print('\n[SYMMETRIC]:')
                bst.symmetric_traversal()
                print('\n[POST-ORDER]:')
                bst.postorder_traversal()
                print('\n[PRE-ORDER]:')
                bst.preorder_traversal()
                print('\n[LEVEL-ORDER]:')
                bst.levelorder_traversal()
                print()
            case 5:
                print(f'\n[HEIGHT of TREE]: {bst.height()}')
            case 6:
                print(f'\n[N° of NODES]: {bst.count_nodes()}')
                print(f'\n[N° of LEAVES]: {bst.count_leaves()}')
            case 7:
                wich_traversal(bst)
            case 8:
                if exit_program() == True:
                    break
                else:
                    continue

run_code()
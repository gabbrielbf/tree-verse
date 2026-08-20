from tree import BinarySearchTree
from menu import numbered_menu, clear_terminal, teach_user, exit_program
from visualizer import wich_traversal

bst = BinarySearchTree()

def run_code():

    teach_user()
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
                print(f'\n[MAX. Value]: {bst.search_max()}')
                print()
                print(f'[MIN. Value]: {bst.search_min()}')
            case 3:
                pass
            case 4:
                print('\n[SYMMETRIC]:')
                bst.symmetric_traversal()
                print('\n[POST-ORDER]:')
                bst.postorder_traversal()
                print('\n[PRE-ORDER]:')
                bst.preorder_traversal()
                print('\n[LEVEL-ORDER]:')
                bst.levelorder_traversal()
            case 5:
                pass
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
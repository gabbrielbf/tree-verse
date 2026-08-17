from lessons import (banner, what_is_nodes, what_is_leaves,
                     what_are_binarytree, what_are_height_depht_paths,
                     minimum_maximum_height, what_are_traversals, what_is_bst,
                     what_are_forests, what_is_subtree)
from utils import read_numeric_option, clear_terminal
# from lessons import 

def numbered_menu():
    """ Numbered menu that displays options dynamically using "enumerate" and "format", 
    returning the chosen option after validation """

    options = [
        'Insert',
        'Search',
        'Remove',
        'Traversals',
        'Height',
        'Visualize',
        'Exit'
    ]

    print('Choose one option bellow: ')
    print('-'*30)
    for index, option in enumerate(options, start=1): # <- This block reduces the repetition of multiple print statements 
        print('{} - {}'.format(index, option))        # print statements and keeps the code clean and elegant
    print('-'*30)

    while True:

        tentative = read_numeric_option()

        if (tentative > 7 or
        tentative < 1): # <- Checks if the user entered something within the suggested options before returning the function value
            print('[ERROR] option not found\n')
            continue
        else:
            break

    return tentative

def traversals():
    """ This function will define according to the user's decision
    which tree traversal will be performed """
    
    traversals = ['Tree',
                'Symmetric',
                'Post-Order',
                'Level-Order',
                'Pre-Order']

    print('Choose your traversal: ')
    print('-'*30)
    for index, traversal in enumerate(traversals, start=1):
        print('{} - {}'.format(index, traversal))
    print('-'*30)

    while True:

        tentative = read_numeric_option()

        if (tentative > 5 or
            tentative < 1):
            print('[ERROR] option not found\n')
            continue
        else:
            break

    return tentative

def lessons():
    """ This function will teach the user about EVERYTHING 
    relevant regarding trees in the data structure """

    lessions = ['What is a NODE?',
                'What is a LEAF?',
                'What are FORESTS?',
                'What is a SUB-TREE?',
                'What are BINARY-TREE?',
                'What are HEIGHT, DEPTH, and PATHS?',
                'What is MINIMUM and MAXIMUM Height?',
                'What are TRAVERSALS?',
                'What is a BINARY-SEARCH-TREE?'
                ]
    
    banner()
    print('What would you like to learn?')
    print('-'*30)
    for index, lession in enumerate(lessions, start=1):
        print('{} - {}'.format(index, lession))
    print('-'*30)

    while True:
    
        tentative = read_numeric_option()

        if (tentative > 9 or
            tentative < 1):
            print('[ERROR] option not found\n')
            continue
        else:
            break

    return tentative

def teach_user():
    """ Function that will put the user in a learning loop
    until they decide they want to use the program by choosing to 'exit' the while. """

    learn_more = 'y'.upper()

    while learn_more:

        clear_terminal()
        match lessons():

            case 1:
                what_is_nodes()
            case 2:
                what_is_leaves()
            case 3:
                what_are_forests()
            case 4:
                what_is_subtree()
            case 5:
                what_are_binarytree()
            case 6:
                what_are_height_depht_paths()
            case 7:
                minimum_maximum_height()
            case 8:
                what_are_traversals()
            case 9:
                what_is_bst()

        again = str(input('Do you want to learn something else? ')).upper()

        if again == 'Y':
            print("Let's learn more!")
            learn_more = again
        else:
            print("Ok, let's move on to practice then\n")
            learn_more = again
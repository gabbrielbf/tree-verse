import os
from lessons import banner
# from lessons import 

def clear_terminal():
    """ Function responsible for clearing the terminal on each iteration """

    input('Press ENTER to continue...')
    os.system('cls' if os.name == 'nt' else 'clear') # <- Clears the terminal screen depending on the operating system
                                                     # (Windows, Linux, or macOS)
    return

def read_numeric_option():
    """ Function that reads a numeric option and handles invalid inputs that are not numbers """

    while True:

        try:
            return int(input('Choose one of the options above -> ')) # <- Returns a numeric value if the user provides a valid input
        except ValueError:
            print('[ERRO] Invalid value!\n')
            continue

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

def teach_user():
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
    
  
import os

def clear_terminal():

    input('Press ENTER to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')

    return

def read_numeric_option():

    while True:

        try:
            return int(input('Choose one of the options above -> '))
        except ValueError:
            print('[ERRO] Invalid value!\n')
            continue

def numbered_menu():

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
    for index, option in enumerate(options, start=1):
        print('{} - {}'.format(index, option))
    print('-'*30)

    while True:

        try:
            tentative = read_numeric_option()

            if (tentative > 7 or
            tentative < 0):
                print('[ERROR] option not found\n')
                continue
        except ValueError:
            print('[ERRO] Invalid value!\n')
            continue
        break

    return tentative

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


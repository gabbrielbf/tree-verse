import os

def clear_terminal():

    input('Press ENTER to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')
import os

def clear_terminal():
    """ Function responsible for clearing the terminal on each iteration """

    input('\nPress ENTER to continue...\n')
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
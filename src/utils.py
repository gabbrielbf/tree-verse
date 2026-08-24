import os, sys, time

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

def tip():
    """ Will only display an optional viewing tip to the user """

    _temp_stack = """ 🧩🔍 Tip: For better visualization of the tree nodes, 
I recommend using the following sequence of values:

[50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93],
this way you will have a perfectly balanced tree of 15 nodes. 

But if you prefer to implement your own values, 
just ignore this message and move on. """
    TIP = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print('=' * 60)

    for char in TIP: # <- this block displays letter by letter of the header
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
    print()

    print('=' * 60)
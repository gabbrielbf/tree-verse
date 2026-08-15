import sys, time

# Responsible for teaching the user everything about the "Tree" data structure.

# _temp_stack.splitlines(): splits the original text into a list of lines (if there are line breaks)
# l.center(60): Centers each line individually, padding the empty spaces to a total width of up to 60 columns
# "\n".join(...): Joins all the centered lines back together into a single string, 
# separating them with line breaks (\n), ensuring the entire banner block is perfectly aligned in the terminal.

# I decided to divide each tree concept into functions to give the user the freedom to choose what 
# they specifically want to learn within the "teach_user" function in the "menu" file

DIVIDER = '=' * 60

def banner():

    _temp_stack = """🌳  WELCOME TO THE TREE-VERSE! 🌳"""
    BANNER = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)
        
    for char in BANNER: # <- this block displays letter by letter of the header
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return 

def what_is_nodes():

    _temp_stack = """ - What are NODES? Connection of non-linear information 
through a specific root. """
    NODES = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)
        
    for char in NODES: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return 

def what_is_leaves():

    _temp_stack = """ - What are LEAVES? Isolated nodes at the end of 
trees with no connections below them. """
    LEAVES = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)

    for char in LEAVES: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return 

def what_is_binarytree():

    _temp_stack = """ - What is a BINARYTREE? It is a tree model that forces 
the developer to provide exactly 2 children for every 
new node that appears in the data structure. """
    BINARYTREE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)

    for char in BINARYTREE: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return

def what_is_height_depht_paths():

    print(DIVIDER)

    _temp_stack = """ - What are Height, Depth, and Paths in TREES 🌳: """
    TITLE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in TITLE: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    _temp_stack = """ 1. Height - It is the length of the path between the root 
and the leaf of greatest depth. """
    HEIGHT = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in HEIGHT: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    _temp_stack = """ 2. Depht - It is the path distance from a given node to be 
selected by the user to the sentinel root of the tree."""
    DEPTH = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in DEPTH: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    _temp_stack = """ 3. Path - It is the sequence of edges (connections) you 
    need to traverse to go from one node to another."""
    PATH = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in PATH: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return

banner()
what_is_nodes()
what_is_leaves()
what_is_binarytree()
what_is_height_depht_paths()
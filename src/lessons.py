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

    return BANNER

def what_is_nodes():

    _temp_stack = """ What are NODES? Connection of non-linear information through a specific root """
    NODES = "\n".join(l.center(57) for l in _temp_stack.splitlines())
    print(NODES)

    return 

def what_is_leaves():

    _temp_stack = """ What are LEAVES? Isolated nodes at the end of trees with no connections below them """
    LEAVES = "\n".join(l.center(57) for l in _temp_stack.splitlines())
    print(LEAVES)

    return 


import sys, time
from utils import clear_terminal

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
        time.sleep(0.02)
    print()

    print(DIVIDER)

    return 

def what_is_nodes():

    _temp_stack = """ - What are NODES? 
Connection of non-linear information through 
a specific root. """
    NODES = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)
        
    for char in NODES: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return 

def what_is_leaves():

    _temp_stack = """ - What are LEAVES 🍃 ? 
Isolated nodes at the end of trees with no 
connections below them. """
    LEAVES = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in LEAVES: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return 

def what_are_forests():

    _temp_stack = """ - What are FORESTS?  🌳🌳🌳:
    Several sets of 2 or more isolated nodes 
    not connected to each other """
    FORESTS = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in FORESTS: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return

def what_is_subtree():

    _temp_stack = """ What is a SUBTREE? 🌳⤵️ :
A subtree is a portion of a tree data structure 
that consists of a specific node 
(called the root of the subtree) and all of its 
descendants (its children, grandchildren, and so on). 
Essentially, every node in a tree can be considered 
the root of its own smaller, self-contained tree. """

    SUBTREE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in SUBTREE:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return

def what_are_binarytree():

    _temp_stack = """ - What is a BINARYTREE 🌳? 
It is a tree model that forces the developer to 
provide exactly 2 children for every new node that 
appears in the data structure. """
    BINARYTREE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in BINARYTREE: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return

def what_are_height_depht_paths():

    clear_terminal()
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
    print()

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

    print(DIVIDER)

    return

def minimum_maximum_height():

    _temp_stack = """ 📌 Maximum Height (or simply Height): 
It is the length of the longest possible path that goes 
from the tree's root to the most distant leaf. Think of 
a family tree or an organizational chart. The maximum 
height represents how many "levels" or steps you need to 
take to get from the top (root) to the deepest element 
of the longest branch. """
    MAXIMUM_HEIGHT = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in MAXIMUM_HEIGHT: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    input('\n Press ENTER to continue...\n')

    _temp_stack = """ 📌 Minimum Height: 
It is the length of the shortest possible path that goes 
from the root to the closest leaf. It is the distance from 
the top to the leaf located at the most superficial 
(least deep) level of the entire structure. """
    MINIMUM_HEIGHT = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in MINIMUM_HEIGHT:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print() 

    print(DIVIDER)

    return

def what_are_traversals():

    _temp_stack = """ - What are TRAVERSALS ⤵️  ? 
Traversals define the order in which the nodes of 
a tree are visited or processed. They are broadly 
categorized into Depth-First Search (DFS) and 
Breadth-First Search (BFS). """
    TITLE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)
    
    for char in TITLE: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()
    
    clear_terminal()
    print(DIVIDER)

    _temp_stack = """ 📌 Depth-First Search (DFS):

    1. Symmetric (Left-Root-Right): 
Traverse the left subtree, visit the root, then 
traverse the right subtree."""
    SYMMETRIC = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in SYMMETRIC:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print()

    _temp_stack = """ 2. Pre-order (Root-Left-Right): 
Visit the root, traverse the left subtree, 
then traverse the right subtree."""
    PREORDER = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in PREORDER:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print()

    _temp_stack = """ 3. Post-order (Left-Right-Root):
Traverse the left subtree, traverse the right 
subtree, and finally visit the root. """
    POSTORDER = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in POSTORDER:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    clear_terminal()
    print(DIVIDER)

    _temp_stack = """ 📌 Breadth-First Search (BFS): 

    1. Level-order (Breadth-first): 
Visits nodes level by level, from left to right, starting 
from the root. It uses a Queue data structure to manage 
the visitation order."""
    LEVELORDER = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in LEVELORDER:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    return

def what_is_bst():

    _temp_stack = """ - What is a BST (Binary Search Tree) 🌳 ?  
A Binary Search Tree (BST) is a node-based data structure 
where each node has at most two children (left and right). 
Its defining property is order:

• All values in the left subtree of a node are smaller 
than the node's value.

• All values in the right subtree are larger 
than the node's value.

• This rule applies recursively to all subtrees. """

    BST = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    clear_terminal()
    print(DIVIDER)

    for char in BST:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    clear_terminal()
    print(DIVIDER)

    _temp_stack = """ How to Find the Minimum and Maximum Value in a BST: 
    
📌 Minimum Value: Start at the root and traverse all the 
way to the left (node.left) until you reach the node 
with no left child.

📌 Maximum Value: Start at the root and traverse all the 
way to the right (node.right) until you reach the node with 
no right child. """

    MINANDMAX = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in MINANDMAX:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    clear_terminal()
    print(DIVIDER)

    _temp_stack = """ 🗑️  The 3 Types of Node Deletion in a BST: 
    
1. ❌  Deleting a Leaf Node (0 children): 

    • The simplest case. The node has no descendants.

    • How to do it: Simply disconnect the node from 
    its parent by setting the parent's respective 
    pointer to null.

------------------------------------------------------------    

2. ❌  Deleting a Node with 1 Child:

    • The node has only one subtree (either left or right).

    • How to do it: Remove the node and let its single 
    child take its place, connecting directly to 
    the deleted node's parent.
    
------------------------------------------------------------

3. ❌  Deleting a Node with 2 Children: 

    • The most complex case, as the node has both left 
    and right subtrees.

    • How to do it: To maintain BST properties, replace 
    the value of the node to be deleted with its in-order 
    successor (the smallest value in the right subtree) or 
    in-order predecessor (the largest value in the 
    left subtree). Then, delete that successor/predecessor 
    from its original position."""
    REMOVE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    for char in REMOVE:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

    print(DIVIDER)

    return


from src.tree import BinarySearchTree

bst = BinarySearchTree()

def test_nodes_behavior():
    """ This test will check if the tree has values on the left 
    that are smaller than the values on the right and the ones 
    on the right are greater than the ones on the left """

    bst.insert(50)
    bst.insert(25)
    bst.insert(75)

    assert bst.root.data == 50 # Checking if the root value is 50
    assert bst.root.left.data == 25
    assert bst.root.right.data == 75

    # Checking left
    assert bst.root.left.data < bst.root.data # If the left node value is smaller than the root
    assert bst.root.data < bst.root.right.data # If the root value is smaller than the right node

    # Checking right
    assert bst.root.right.data > bst.root.data 
    assert bst.root.data > bst.root.left.data 

def test_removing_nodes_behavior():
    """ This test will check the logic 
    for removal and finding the substitute """

    pass

    
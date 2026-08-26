from src.tree import BinarySearchTree

bst = BinarySearchTree()

def test_nodeleft_behavior():
    """ This test will check if the tree has
    smaller values on the left than on the right """

    bst.insert(50)
    bst.insert(25)
    bst.insert(75)

    assert bst.root.data == 50 # Checking if the root value is 50
    assert bst.root.left.data == 25
    assert bst.root.right.data == 75
    assert bst.root.left.data < bst.root.data # Checking if the left node value is smaller than the root
    assert bst.root.data < bst.root.right.data # Checking if the root value is smaller than the right node
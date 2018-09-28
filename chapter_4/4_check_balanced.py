import unittest

from data_structures.trees_and_graphs.binary_search_tree import (
    BinarySearchTree
)


def recursive_helper(current_node, is_balanced):
    """Recursively check if left and right trees of current node are balanced

    Parameters
    ----------
    current_node : Node
        Node to check in a binary search tree
    is_balanced : bool
        True if all nodes checked so far are balanced, False if any nodes
        checked so far are unbalanced

    Returns
    -------
    height : int
        Height of current node
    is_balanced : bool
        True if all nodes checked so far are balanced, False if any nodes
        checked so far are unbalanced
    """
    # Break case for recursion:
    if current_node is None:
        return 0, is_balanced

    # Recursively get heights of sub-trees at left and right nodes, checking
    # that both sub-trees are balanced
    left_height, is_balanced_left = recursive_helper(
        current_node.left_node, is_balanced
    )
    if not is_balanced_left:
        return None, is_balanced_left
    right_height, is_balanced_right = recursive_helper(
        current_node.right_node, is_balanced
    )
    if not is_balanced_right:
        return None, is_balanced_right

    # Check that heights of left and right sub-trees don't differ by more than
    # 1
    if abs(left_height - right_height) > 1:
        return None, False

    return max(left_height, right_height) + 1, is_balanced


def check_balanced(tree):
    """Check if a binary search tree is balanced

    Tree is balanced if the left and right sub-tree of every node has heights
    that do not differ from each other by more than 1. Height is the number of
    connections from the current node to the leaf node, along the most direct
    (downward) route.

    Parameters
    ----------
    tree : BinarySearchTree
        Tree to check

    Returns
    -------
    is_balanced : bool
        True if all nodes in tree are balanced, False if any nodes are
        unbalanced
    """
    node, is_balanced = recursive_helper(tree.root, True)

    return is_balanced


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        ([9, 7, 10, 6, 8, 11], True),
        ([9, 7, 11, 5, 8, 3], False),
    ]

    def test_check_balanced(self):
        for test_input, test_output in self.data:
            # Generate tree from array
            tree = BinarySearchTree()
            [tree.insert(i) for i in test_input]

            self.assertEqual(
                check_balanced(tree), test_output
            )


if __name__ == '__main__':

    unittest.main()

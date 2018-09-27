import unittest
import math


from data_structures.trees_and_graphs.binary_search_tree import (
    BinarySearchTree, Node
)

class Node:

    def __init__(self, item):
        self.right_node = None
        self.left_node = None
        self.data = item

    def __str__(self):
        return '('+str(self.left_node)+':L ' + "V:" + str(self.data) + " R:" + str(self.right_node)+')'


def initiateArrayToBinary(array):
    root = arrayToBinary(array, 0, len(array) - 1)
    tree = BinarySearchTree()
    tree.root = root
    return tree


def arrayToBinary(array, start, end):
    if start > end:
        return None
    mid = int((start + end) / 2)
    root = Node(array[mid])
    root.left_node = arrayToBinary(array, start, mid - 1)
    root.right_node = arrayToBinary(array, mid + 1, end)
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(initiateArrayToBinary(testArray))


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def _get_max_depth(self, current_node):
        """Helper function to find the depth of a binary search tree

        Works by recursively exploring all nodes in tree, keeping track of
        deepest level

        Parameters
        ----------
        current_node : Node
            Current root of (sub-)tree

        Returns
        -------
        depth_count : int
            Deepest level in (sub)-tree
        """
        # Base case, at leaf node
        if current_node is None:
            return 0
        else:
            # Compute depth of left and right sub-trees
            left_depth = self._get_max_depth(current_node.left_node)
            right_depth = self._get_max_depth(current_node.right_node)

            # Return larger of two depths, + 1 (since explored another level in
            # this call)
            return max(left_depth, right_depth) + 1

    def _test_helper(self, func_to_test):
        """Test a function that creates a minimal binary search tree from a
        sorted array

        Parameters
        ----------
        func_to_test : func
            Function being tested
        """
        # Set up arrays to insert
        arrays = [
            list(range(1, 16)),
            list(range(1, 17)),
            [1, 2, 4, 5, 6, 8, 9, 14, 17, 19, 20, 21]
        ]

        for array in arrays:
            print(array)
            tree = func_to_test(array)
            tree.traverse()

            # Compute expected tree depth and actual depth
            expected_depth = math.ceil(math.log(len(array), 2.0))
            actual_depth = self._get_max_depth(tree.root)
            print(actual_depth)

            self.assertEqual(expected_depth, actual_depth)

    def test_create_minimal_tree(self):
        """Test my own create minimal tree function
        """
        self._test_helper(initiateArrayToBinary)
        pass


if __name__ == '__main__':

    unittest.main()

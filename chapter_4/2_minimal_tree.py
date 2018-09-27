import math
import unittest

from data_structures.trees_and_graphs.binary_search_tree import (
    BinarySearchTree, Node
)


def _recursive_helper(tree, start_index, end_index, array):
    """Recursively insert middle element in sub-array into a binary search tree

    Parameters
    ----------
    tree : BinarySearchTree
        Tree to insert elements into
    start_index : int
        Index in array denoting start of sub-array
    end_index : int
        Index in array denoting end of sub-array
    array : list of any
        Array that we are inserting elements into tree from. Can contain any
        Python object that allows comparison.

    Returns
    -------
    tree : BinarySearchTree
        Input tree if with relevant elements from array inserted
    """
    # Break case, when start index and end index overlap
    if end_index < start_index:
        return tree

    # Find and insert mid element
    mid_index = int((start_index + end_index) / 2)
    tree.insert(array[mid_index])

    # Recusively insert mid element of sub-array on left half of this
    # sub-array
    tree = _recursive_helper(tree, start_index, mid_index - 1, array)

    # Recusively insert mid element of sub-array on right half of this
    # sub-array
    tree = _recursive_helper(tree, mid_index + 1, end_index, array)

    return tree


def create_minimal_tree(array):
    """Insert elements in sorted input array into a binary search tree, such
    that the tree has the minimum depth possible

    Parameters
    ----------
    array : list of any
        Array that we are inserting elements into tree from. Must be sorted
        (smallest to largest). Can contain any object that allows comparison.

    Returns
    -------
    tree : BinarySearchTree
        Input tree if with elements from array inserted
    """
    # Initialise binary search tree
    tree = BinarySearchTree()

    # Recursively insert elements
    tree = _recursive_helper(tree, 0, len(array) - 1, array)

    return tree


def solution_recursive_helper(array, start_index, end_index):
    """Recursively add middle elements from sub-array into left_node and
    right_node of current node in tree

    Parameters
    ----------
    array : list of any
        Array that we are inserting elements into tree from. Can contain any
        Python object that allows comparison.
    start_index : int
        Index in array denoting start of sub-array
    end_index : int
        Index in array denoting end of sub-array
    """
    # Break case, when indices overlap
    if end_index < start_index:
        return None

    # Get index of middle element
    mid_index = int((start_index + end_index) / 2)
    node = Node(array[mid_index])
    # Recursively insert elements into left node
    node.left_node = solution_recursive_helper(
        array, start_index, mid_index - 1
    )
    # Recursively insert elements into right node
    node.right_node = solution_recursive_helper(
        array, mid_index + 1, end_index
    )

    return node


def create_minimal_tree_solution(array):
    """Insert elements in sorted input array into a binary search tree, such
    that the tree has the minimum depth possible

    Improves upon create_minimal_tree() implementation (which is O(log(n))) by
    avoiding traversing entire tree every time an insertion is required.
    Instead, it recursively adds the left_node and right_node to the
    current_node, effectively keeping track of where we are as we build the
    tree. This solution is O(n).

    Parameters
    ----------
    array : list of any
        Array that we are inserting elements into tree from. Must be sorted
        (smallest to largest). Can contain any object that allows comparison.

    Returns
    -------
    tree : BinarySearchTree
        Input tree if with elements from array inserted
    """
    # Recursively insert elements into left and right nodes
    root_node = solution_recursive_helper(array, 0, len(array) - 1)

    # Create binary search tree and put the root into it
    tree = BinarySearchTree()
    tree.root = root_node

    return tree


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

    def _get_expected_depth(self, array):
        """Compute the expected maximum depth of a minimal binary search tree,
        created from a sorted array

        Parameters
        ----------
        array : list of any
            Array that tree is built from. Must be sorted (smallest to
            largest). Can contain any object that allows comparison.

        Returns
        -------
        int
            Maximum expected depth of binary search tree
        """
        log_arr_len = math.log(len(array), 2.0)
        if int(log_arr_len) == log_arr_len:
            return int(log_arr_len + 1)
        else:
            return math.ceil(log_arr_len)

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
            tree = func_to_test(array)

            # Compute expected tree depth and actual depth
            expected_depth = self._get_expected_depth(array)
            actual_depth = self._get_max_depth(tree.root)

            self.assertEqual(expected_depth, actual_depth)

    def test_create_minimal_tree(self):
        """Test my own create minimal tree function
        """
        self._test_helper(create_minimal_tree)
        pass

    def test_create_minimal_tree_solution(self):
        """Test book's create minimal tree solution
        """
        self._test_helper(create_minimal_tree_solution)


if __name__ == '__main__':

    unittest.main()

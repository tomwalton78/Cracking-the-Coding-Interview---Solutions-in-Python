import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList
from data_structures.trees_and_graphs.binary_search_tree import (
    BinarySearchTree
)


def recursive_helper(current_node, depth, array):
    """Recursively add node to linked list that corresponds to the current
    depth

    Parameters
    ----------
    current_node : Node
        Node in a binary (search) tree
    depth : int
        Current depth in tree
    array : list of LinkedList
        List of linked lists, with 1 linked list per depth in tree

    Returns
    -------
    array : list of LinkedList
        Updated input list of linked lists
    """
    # Break case, when leaf node is reached
    if current_node is None:
        return array

    # Create empty linked list if required
    if len(array) - 1 < depth:
        array.extend([LinkedList()])

    # Add node to relevant linked list
    array[depth].prepend(current_node.data)

    # Recursively explore left node
    array = recursive_helper(current_node.left_node, depth + 1, array)
    # Recursively explore right node
    array = recursive_helper(current_node.right_node, depth + 1, array)

    return array


def generate_list_of_depths(tree):
    """Given a binary tree, create a list of linked lists, where each linked
    list has all of nodes at a certain depth in the tree

    Parameters
    ----------
    tree : BinarySearchTree
        Tree to process

    Returns
    -------
    array : list of LinkedList
        List of linked lists, with 1 linked list per depth in tree
    """
    return recursive_helper(tree.root, 0, [LinkedList()])


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def test_generate_list_of_depths(self):
        """Test list_of_depths function against expected output

        Order of elements in a linked list does not matter here.
        """

        # Define arrays to be used to fill binary search trees
        input_arrays = [
            [7, 5, 9],
            [9, 10, 5, 3, 6, 1]
        ]

        # Define ouput arrays, for elements expected in each linked list
        output_arrays = [
            [[7], [5, 9]],
            [[9], [5, 10], [3, 6], [1]]
        ]

        for input_array, output_array in zip(input_arrays, output_arrays):
            # Generate input binary search tree
            bst = BinarySearchTree()
            [bst.insert(i) for i in input_array]
            # Generate list of linked lists
            list_of_linked_lists = generate_list_of_depths(bst)

            # Check that all linked lists are as expected
            for i, linked_list in enumerate(list_of_linked_lists):

                # Convert linked list to list
                to_str = linked_list.__str__().split('\n')[1:][0]
                to_list = to_str.replace(' ', '').split(',')
                to_list = [int(item) for item in to_list]

                # Validate number of elements
                if len(output_array[i]) != len(to_list):
                    self.fail('Incorrect number of elements in linked lists')

                # Validate that elements are as expected
                for item in output_array[i]:
                    if item not in to_list:
                        self.fail(
                            'Not all elements required are in linked lists'
                        )


if __name__ == '__main__':

    unittest.main()

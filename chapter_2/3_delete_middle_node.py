import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


def delete_middle_node(node):
    """Given only access to middle node (not start or end node) in a
    LinkedList, delete it

    Note: no access to head node

    Parameters
    ----------
    node : Node in LinkedList
        Node to delete
    """
    # Copy data first, before next node reference
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        (
            (LinkedList(input_arr=[1, 2, 2, 5, 6, 2]), 2),
            LinkedList(input_arr=[1, 2, 5, 6, 2])
        ),
        (
            (LinkedList(input_arr=['a', 'b', 'c', 'd', 'e']), 3),
            LinkedList(input_arr=['a', 'b', 'c', 'e'])
        ),
    ]

    def test_delete_middle_node(self):
        for test_input, test_output in self.data:

            # Fin node to delete, to input into function
            node_to_delete = test_input[0].head
            for i in range(test_input[1]):
                node_to_delete = node_to_delete.next_node

            # Perform deletion
            delete_middle_node(node_to_delete)

            # Check resulting linked list is as expected
            self.assertEqual(
                test_input[0].__str__(), test_output.__str__()
            )


if __name__ == '__main__':

    unittest.main()

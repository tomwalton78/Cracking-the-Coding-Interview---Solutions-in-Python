import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


def remove_dups(linked_list):
    """Remove duplicate values from a linked list

    Uses a hash table to store values previously found, and walks through
    linked list, deleting duplicates vals.

    Parameters
    ----------
    linked_list : LinkedList
        Linked list to remove duplicates from

    Returns
    -------
    linked_list : LinkedList
        Input linked list, with duplicates removed
    """
    # Handle empty linked list
    if linked_list.head is None:
        return linked_list

    # Initialise hash table to contain values found
    vals_found = {}

    # Start at head
    current_node = linked_list.head
    # Add head val to vals_found
    vals_found[current_node.data] = True

    # Walk through linked list, from head to tail
    while current_node.next_node is not None:
        # Check next node's value, to see if it is a duplicate
        next_node = current_node.next_node
        if next_node.data in vals_found:
            # Delete next node
            current_node.next_node = next_node.next_node
            # Stick to current_node, don't update it, since its next_node has
            # changed
        else:
            # Add val to vals_found
            vals_found[next_node.data] = True
            # Go to next node
            current_node = next_node

    return linked_list


def remove_dups_v2(linked_list):
    """Remove duplicate values from a linked list

    Constraint: no temporary buffer is allowed
    Therefore, brute force: for each element, delete all subsequent elements
    with same value

    Parameters
    ----------
    linked_list : LinkedList
        Linked list to remove duplicates from

    Returns
    -------
    linked_list : LinkedList
        Input linked list, with duplicates removed
    """
    # Handle empty linked list
    if linked_list.head is None:
        return linked_list

    # Start at head (pointer 1)
    current_node = linked_list.head

    # Walk through linked list from head to tail, deleting subsequent elements
    # with same value at each element
    while current_node.next_node is not None:
        # Use another pointer (pointer 2) to search rest of linked list for
        # duplicates
        searching_node = current_node
        while searching_node.next_node is not None:
            # Check next node for duplicate value
            if searching_node.next_node.data == current_node.data:
                # Delete node, if has same value as current node
                searching_node.next_node = searching_node.next_node.next_node
                # Don't change searching node, since deleted its next node, so
                # need to check its new next node
            else:
                # Update searching_node
                searching_node = searching_node.next_node

        # Update current_node
        current_node = current_node.next_node

    return linked_list


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        (LinkedList(input_arr=[1, 2, 2]), LinkedList(input_arr=[1, 2])),
        (LinkedList(input_arr=[1, 2, 3]), LinkedList(input_arr=[1, 2, 3])),
        (LinkedList(input_arr=[1]), LinkedList(input_arr=[1])),
        (
            LinkedList(input_arr=['a', 'b', 'b']),
            LinkedList(input_arr=['a', 'b'])
        ),
        (
            LinkedList(input_arr=list('abbacdeefaab')),
            LinkedList(input_arr=list('abcdef'))
        ),
        (LinkedList(input_arr=[]), LinkedList(input_arr=[])),
    ]

    def test_remove_dups(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                remove_dups(test_input).__str__(), test_output.__str__()
            )

    def test_remove_dups_v2(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                remove_dups(test_input).__str__(), test_output.__str__()
            )


if __name__ == '__main__':

    unittest.main()

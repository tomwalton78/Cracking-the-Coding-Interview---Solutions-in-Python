import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


def return_kth_to_last(linked_list, k):
    """Find kth to last element in linked list and return it

    Uses two pointers, with first finding element k, the 2nd finding kth to
    last element

    Parameters
    ----------
    linked_list : LinkedList
        Linked list to search through
    k : int
        Kth to last element to find

    Returns
    -------
    any
        Value at kth to last element in linked list
    """
    # Handle special case of empty linked list
    if linked_list.head is None:
        raise Exception('Invalid query. LinkedList is empty.')

    # Set pointer 1 to head of linked list
    p1 = linked_list.head
    # Initialise counter
    counter = 0

    # Iterate through linked list until element k is reached
    try:
        while counter < k:
            p1 = p1.next_node
            counter += 1
    except AttributeError:
        raise AttributeError('k is too large for the linked list given')

    # Set 2nd pointer to start of linked list
    p2 = linked_list.head
    # Keep iterating both pointers through linked list until 2nd pointer
    # reaches end of linked list
    while p1.next_node is not None:
        p1 = p1.next_node
        p2 = p2.next_node

    return p2.data


def recursive_helper(current_node, k):
    """Recursively look for kth to last node, recursing until end of linked
    list, then going back up recursion stack, incrementing k until kth to last
    node is found.

    Parameters
    ----------
    current_node : Node in LinkedList
        Last node that was visited (previous node in linked list)
    k : int
        Kth to last element to find

    Returns
    -------
    index : int
        Keeps track of how many nodes from end you are in the stack,
        incremented by one on each recursive call.
    """
    # Break case for recursion, starting index counter; breaks when last node
    # is reached
    if current_node.next_node is None:
        if k == 0:
            return -1, current_node.data
        else:
            return 1, None

    # Recursively update index
    index, value = recursive_helper(current_node.next_node, k)

    # Break case for recursion, kth to last element found
    if index == k:
        return -1, current_node.data

    # Check for special index value, that signifies value has been found, and
    # simply going back up recursion stack with it
    if index == -1:
        return -1, value

    # Increment index when recursive call returns
    return index + 1, None


def return_kth_to_last_v2(linked_list, k):
    """Find kth to last element in linked list and return it

    Uses recursive implementation. Less efficient than first method (still O(n)
    time, but O(n) space (cf. O(1) space for first solution)), but good
    practice nonetheless.

    Parameters
    ----------
    linked_list : LinkedList
        Linked list to search through
    k : int
        Kth to last element to find

    Returns
    -------
    any
        Value at kth to last element in linked list
    """
    # Handle special case of empty linked list
    if linked_list.head is None:
        raise Exception('Invalid query. LinkedList is empty.')

    # Run recursive search
    index, value = recursive_helper(linked_list.head, k)

    # Check for kth to last element not being found (i.e. index never equalled
    # k)
    if index != -1:
        raise Exception('k is too large for the linked list given')
    else:
        return value


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        ((LinkedList(input_arr=[1, 2, 3, 4, 5]), 2), 3),
        ((LinkedList(input_arr=[1, 2, 3, 4, 5]), 0), 5),
        ((LinkedList(input_arr=[1, 2, 3, 4, 5]), 4), 1),
    ]

    def test_return_kth_to_last(self):
        # Test data inputs and outputs
        for test_input, test_output in self.data:
            self.assertEqual(
                return_kth_to_last(test_input[0], test_input[1]), test_output
            )

        # Test empty LinkedList
        with self.assertRaises(Exception):
            return_kth_to_last(LinkedList(), 0)

        # Test k that is too large
        with self.assertRaises(AttributeError):
            return_kth_to_last(LinkedList(input_arr=[1, 2, 3, 4, 5]), 10)

    def test_return_kth_to_last_v2(self):
        # Test data inputs and outputs
        for test_input, test_output in self.data:
            self.assertEqual(
                return_kth_to_last_v2(
                    test_input[0], test_input[1]
                ), test_output
            )

        # Test empty LinkedList
        with self.assertRaises(Exception):
            return_kth_to_last_v2(LinkedList(), 0)

        # Test k that is too large
        with self.assertRaises(Exception):
            return_kth_to_last_v2(LinkedList(input_arr=[1, 2, 3, 4, 5]), 10)


if __name__ == '__main__':

    unittest.main()

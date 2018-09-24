import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList

# Note: another solution (from book) is to create a new linked list and either
# prepend or append elements to that depending on if they are less than the
# partition value (then prepend), or greater (append). Note that for append
# should keep track of tail of linked list, for O(1) insertion. To save space
# could then delete element from main linked list.
# My solution is similar, but works in place. It is perhaps more verbose, but
# has same time and space complexity. So essentially as efficient, hence book's
# solution not implemented.


def partition(linked_list, partition_val):
    """Ensure that all elements with values less than partition_val, come
    before all elements with values greater than or equal to partition val, in
    a linked list.

    Parameters
    ----------
    linked_list : LinkedList
        Linked list to partition
    partition_val : any
        Any object that can be stored in LinkedList, and allows comparison

    Returns
    -------
    linked_list : LinkedList
        Partitioned input linked list
    """
    # Handle empty linked list
    if linked_list.head is None:
        raise Exception('Empty linked list, cannot perform operation')

    # Keep track of intersection between left and right half of linked list
    # using pointer 1
    p1 = linked_list.head

    # Use pointer 2 to walk through linked list, starting at node after head
    p2 = linked_list.head.next_node
    p2_prev = linked_list.head  # keep track of node before p2 pointer; needed
    # to delete last element in linked list
    while p2 is not None:
        if p2.data < partition_val:
            # Put p2 node at beginning of linked list
            linked_list.prepend(p2.data)
            # Delete p2 node
            # Handle being at end of linked list
            if p2.next_node is None:
                p2_prev.next_node = None
                p2 = None
            else:
                p2.data = p2.next_node.data
                p2.next_node = p2.next_node.next_node
        else:
            # p2 value is >= partition_val, so leave it where it is
            # Go to next node
            p2_prev = p2
            p2 = p2.next_node

    return linked_list


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        (LinkedList(input_arr=[1, 2, 2, 5, 6, 2]), 3),
        (LinkedList(input_arr=[1, 2, 3, 1, 2, 3, 5]), 2),
        (LinkedList(input_arr=[10, 21, 21, 56, 66, 20]), 5),
        (LinkedList(input_arr=[1, 2, 3, 1, 2, 3, 5]), 20),
        (LinkedList(input_arr=[1, 3]), 2),
        (LinkedList(input_arr=[3, 1]), 2)
    ]

    def _is_partitioned(self, linked_list, partition_val):
        """Tests to see if linked list is partitioned properly

        Parameters
        ----------
        linked_list : LinkedList
            Partitioned linked list
        partition_val : any
            Any object that can be stored in LinkedList, and allows comparison

        Returns
        -------
        bool
            True if linked_list is partitioned correctly, False otherwise
        """
        current_node = linked_list.head
        in_right_half = False  # Turns to True when first element with
        # value >= partition_val has been found in linked_list

        # Walk through linked list, checking values
        while current_node is not None:
            # Note: an optimisation would be to stop performing this check once
            # in_right_half is True (use separate while loop); not implemented
            if current_node.data >= partition_val and not in_right_half:
                in_right_half = True
            if in_right_half:
                if current_node.data < partition_val:
                    return False

            # Go to next node
            current_node = current_node.next_node

        return True

    def test_partition(self):
        for test_input in self.data:

            result = partition(test_input[0], test_input[1])
            self.assertTrue(self._is_partitioned(result, test_input[1]))

        # Test empty LinkedList
        with self.assertRaises(Exception):
            partition(LinkedList(), 3)


if __name__ == '__main__':

    unittest.main()

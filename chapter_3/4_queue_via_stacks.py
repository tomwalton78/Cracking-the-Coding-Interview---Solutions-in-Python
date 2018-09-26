import unittest

from data_structures.stacks_and_queues.stack import Stack


class MyQueue():
    """Queue implemented using 2 stacks

    Swap all elements between stacks when need to swap between pushing and
    popping
    """

    def __init__(self):
        """Initialise push and pop stacks
        """
        # Create stack elements need to be on when adding to queue
        self.add_stack = Stack()
        # Create stack elements need to be on when removing from queue
        self.remove_stack = Stack()
        # Use boolean to track last operation
        self.just_added = True
        # Note: could just check if relevant stack is empty, rather than using
        # this flag

    def _swap_elements(self, stack_1, stack_2):
        """Put all elements in stack_1 into stack_2

        Parameters
        ----------
        stack_1 : Stack
            Stack to remove elements from
        stack_2 : Stack
            Stack to put elements onto
        """
        while not stack_1.is_empty():
            element = stack_1.pop()
            stack_2.push(element)

    def add(self, data):
        """Add element to back of queue, swapping stacks if required

        Parameters
        ----------
        data : any
            Data to store in queue; can be any python object
        """
        if not self.just_added:
            # Need to swap stacks, so we can add to back of queue
            self._swap_elements(self.remove_stack, self.add_stack)
            # Update bool
            self.just_added = True

        # Add element to back of queue
        self.add_stack.push(data)

    def remove(self):
        """Remove element from front of queue, swapping stack if required

        Returns
        -------
        data : any
            Data at front of queue; can be any Python object.
        """
        if self.just_added:
            # Need to swap stacks, so we can remove from front of queue
            self._swap_elements(self.add_stack, self.remove_stack)
            # Update bool
            self.just_added = False

        # Remove element
        return self.remove_stack.pop()


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def test_MyQueue(self):
        """Test MyQueue on basic operations
        """

        q = MyQueue()

        # Test popping from empty queue
        with self.assertRaises(Exception):
            q.remove()

        # Test inserting elements
        try:
            q.add(2)
        except Exception:
            self.fail("add() method raised Exception unexpectedly!")
        try:
            q.add(7)
        except Exception:
            self.fail("add() method raised Exception unexpectedly!")

        # Test removing an element
        self.assertEqual(q.remove(), 2)

        try:
            q.add(5)
            q.add(6)
        except Exception:
            self.fail("add() method raised Exception unexpectedly!")

        # Test removing multiple elements
        self.assertEqual(q.remove(), 7)
        self.assertEqual(q.remove(), 5)
        self.assertEqual(q.remove(), 6)

        # Ensure queue is empty
        with self.assertRaises(Exception):
            q.remove()


if __name__ == '__main__':

    unittest.main()

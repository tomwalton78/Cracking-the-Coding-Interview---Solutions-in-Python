import unittest

from data_structures.stacks_and_queues.stack import Stack


class SubStack(Stack):
    """Class to represent stack that tracks num of elements

    Wraps Stack class
    """

    def __init__(self):
        """Initialise in same way as Stack, but setup variable to track num of
        elements in stack
        """
        super().__init__()
        self.num_elements = 0

    def push(self, data):
        """Pushes data to stack, updating num_elements

        Parameters
        ----------
        data
            Data to store in stack
        """
        super().push(data)
        self.num_elements += 1

    def pop(self):
        """Remove and return top item from stack, updating num_elements

        Returns
        -------
        data : any
            Data at top of stack. Can be any Python object.
        """
        data = super().pop()
        self.num_elements -= 1
        return data


class SetOfStacks():
    """Class to store a single stack in an array of stacks, with no stack
    bigger than a set threshold
    """

    def __init__(self, stack_capacity):
        """Set up array of stacks

        Parameters
        ----------
        capacity : int
            Max no. of elements in a single SubStack
        """
        self.stacks = []
        self.stack_capacity = stack_capacity

    def push(self, data):
        """Push an element to appropriate SubStack

        Parameters
        ----------
        data : any
            Data to store in stack. Can be any Python object.
        """
        # Handle special case of no stacks present
        if len(self.stacks) == 0:
            self.stacks.append(SubStack())
        # Check if last stack in list is at capacity
        elif self.stacks[-1].num_elements == self.stack_capacity:
            self.stacks.append(SubStack())

        # Push data onto last stack in list
        self.stacks[-1].push(data)

    def pop(self):
        """Pop item from last stack, deleting stacks as necessary

        Returns
        -------
            Data at top of stack
        """
        # Check stacks exist
        if len(self.stacks) == 0:
            raise Exception('Unable to pop, no elements in stack.')

        # Perform pop operation on last SubStack in list
        data = self.stacks[-1].pop()

        # Delete last SubStack if required
        if self.stacks[-1].num_elements == 0:
            del self.stacks[-1]

        return data

    def _pop_at(self, index):
        """Pops item from stacks array at specified index.

        Parameters
        ----------
        index : int
            Index in stacks array of SubStack to pop from
        """
        # Perform pop operation on relevant SubStack
        data = self.stacks[index].pop()

        # Delete stack we just popped from if it is now empty
        if self.stacks[index].num_elements == 0:
            del self.stacks[index]

        return data


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def test_SetOfStacks(self):
        """Test operations of SetOfStacks class
        """

        s = SetOfStacks(3)

        # Test empty stack
        with self.assertRaises(Exception):
            s.pop()

        # Test inserting elements
        try:
            s.push(2)
        except Exception:
            self.fail("push() method raised Exception unexpectedly!")
        try:
            [s.push(i) for i in range(3, 10)]
        except Exception:
            self.fail("push() method raised Exception unexpectedly!")

        # Test pop
        self.assertEqual(s.pop(), 9)
        self.assertEqual(s.pop(), 8)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 6)

        # Test pop_at method
        self.assertEqual(s._pop_at(0), 4)


if __name__ == '__main__':

    unittest.main()

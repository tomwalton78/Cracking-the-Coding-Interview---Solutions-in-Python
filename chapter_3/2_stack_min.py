import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList
from data_structures.stacks_and_queues.stack import Stack


class StackData():
    """Class to represent a piece of data in StackMin

    Holds info about data contained, and minimum of all elements at this level
    of stack and below
    """

    def __init__(self, data, min_val):
        """Input values

        Parameters
        ----------
        data : Any
            Any Python object that allows comparison
        min_val : any
            Minimum value of sub-stack. Can be any Python object that allows
            comparison
        """
        self.data = data
        self.min_val = min_val


class StackMin(LinkedList):
    """Class to represent a stack data structure, with O(1) method for getting
    min value in stack.
    """

    def get_min(self):
        """Returns min value in stack

        Returns
        -------
        min_val : any
            Minimum value of sub-stack. Can be any Python object that allows
            comparison
        """
        if self.head is None:
            raise Exception('{} is empty.'.format(self.__name__))

        return self.head.data.min_val

    def push(self, data):
        """Add item (data) to top of stack (i.e. to head of LinkedList).

        Ensure to add info about min of sub-array

        Parameters
        ----------
        data
            Data to store in stack.
        """
        # Find exising min_val
        # Handle special case of empty stack
        if self.head is None:
            min_val = data
        else:
            min_val = self.get_min()

        if data < min_val:
            min_val = data

        # Create StackData to represent data point, and push to stack
        self.prepend(StackData(data, min_val))

    def _delete_head(self):
        """Delete head node of LinkedList.
        """
        self.head = self.head.next_node

    def pop(self):
        """Remove and return the top item from the stack.

        Returns
        -------
            Data at head of LinkedList
        """
        if self.head is None:
            raise Exception('{} is empty.'.format(self.__name__))

        # Retrieve head node data, then delete head node
        data = self.head.data.data
        self._delete_head()

        return data


class StackMin2(Stack):
    """More efficient version of StackMin

    Doesn't store extra piece of data (min value) at every node, since this is
    v. inefficient if, say, first node is min value, and there are many nodes
    above it.

    Instead, use another stack to keep track of min value when it changes. Note
    that adding another element with value equal to the current min value does
    add to this stack, since otherwise removing this element would break
    get_min() (this wasn't clear in book's solution).
    ^Above solution based on book's solution.
    """

    def __init__(self):
        """Initialise stack as is done for Stack, but also introduce stack
        to track min values
        """
        # Initialise Stack
        super().__init__()

        # Use this stack to track min vals
        self.min_vals = Stack()

    def get_min(self):
        """Returns min value in stack

        Returns
        -------
        min_val : any
            Minimum value of sub-stack. Can be any Python object that allows
            comparison.
        """
        return self.min_vals.peek()

    def push(self, data):
        """Add item (data) to top of stack (i.e. to head of Stack).

        Ensure to add info about min of sub-array

        Parameters
        ----------
        data
            Data to store in stack.
        """
        # Find exising min_val
        # Handle special case of empty stack
        if self.head is None:
            self.min_vals.push(data)
        else:
            min_val = self.get_min()
            if data <= min_val:
                self.min_vals.push(data)

        # Add data to stack
        self.prepend(data)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns
        -------
        any
            Data at head of Stack. Can be any Python object that allows
            comparison.
        """
        if self.head is None:
            raise Exception('{} is empty.'.format(self.__name__))

        # Retrieve head node data, then delete head node
        data = self.head.data
        self._delete_head()

        # Remove element from min_vals stack, if required
        if data == self.min_vals.peek():
            self.min_vals.pop()

        return data


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    def _test_helper(self, stack_class):
        """Test stack min object of specified class

        Parameters
        ----------
        stack_class : Class
            Used to construct instance of class to test
        """

        s = stack_class()

        # Test empty stack
        with self.assertRaises(Exception):
            s.get_min()
        with self.assertRaises(Exception):
            s.pop()

        # Test inserting elements
        try:
            s.push(2)
        except Exception:
            self.fail("push() method raised Exception unexpectedly!")
        try:
            s.push(7)
        except Exception:
            self.fail("push() method raised Exception unexpectedly!")
        try:
            s.push(1)
        except Exception:
            self.fail("push() method raised Exception unexpectedly!")

        # Test getting min
        self.assertEqual(s.get_min(), 1)

        # Test pop
        self.assertEqual(s.pop(), 1)

        # Test get min updated
        self.assertEqual(s.get_min(), 2)

    def test_StackMin(self):
        self._test_helper(StackMin)

    def test_StackMin2(self):
        self._test_helper(StackMin2)


if __name__ == '__main__':

    unittest.main()

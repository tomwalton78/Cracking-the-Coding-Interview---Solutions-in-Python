class StackInfo():
    """Class contain info needed to use a stack implemented as part of the
    MultiStack class.
    """

    def __init__(self, index, capacity=1):
        """Initialise info about stack, essentially showing where it is inside
        the main array of the MutliStack class

        Parameters
        ----------
        index : int
            Starting index of stack in main array of MultiStack class
        capacity : int, optional
            No. of elements in main array to initially allocate to this stack
            in main array of MultiStack class
        """
        self.bottom_index = index
        self.top_index = index
        self.end_of_capacity_index = index + capacity

    def get_height(self):
        """Returns num of elements in stack

        Returns
        -------
        int
            No. of elements in stack
        """
        return self.top_index - self.bottom_index

    def get_capacity(self):
        """Returns how many elements in main array of multiStack class are
        allocated to this stack

        Returns
        -------
        int
            No. of elements that can be in stack before size needs readjusting
        """
        return self.end_of_capacity_index - self.bottom_index


class MultiStack():
    """Class to contain mutliple stacks, with all elements stored in a single
    array, and stack size flexibly increasing as required
    """

    def __init__(self, starting_length=10):
        """Initialise MultiStack, with no stacks created yet

        Parameters
        ----------
        starting_length : int, optional
            Starting length of main array that holds elements of all stacks
        """
        # Set up dictionary to contain stack ids, and correponding StackInfo
        # objects
        self.stacks = {}

        # Initialise aray that holds all elements of all stacks
        self.main_array = [None] * starting_length

        # Store reference to last (rightmost) stack in main_array; useful when
        # adding new stacks
        self.last_stack = None

    def _ensure_space_is_allocated(self, extra_space_required):
        """Doubles size of main array, if required, given as input how much
        space after last stack is required

        Parameters
        ----------
        extra_space_required : int
            Extra capacity that main array must support, after last stack
        """
        # Allocate plenty of space for stack in main array (double what is
        # required, at most)
        if self.last_stack is None:
            if len(self.main_array) < extra_space_required:
                # Double size of main array
                self.main_array.extend([None] * len(self.main_array))
        else:
            space_available = len(self.main_array) -
            self.last_stack.end_of_capacity_index
            if space_available < extra_space_required:
                # Double size of main array
                self.main_array.extend([None] * len(self.main_array))

    def _add_element(self, stack_id, element):
        """Add single element to specified stack, extending main array
        appropriately if required.

        Parameters
        ----------
        stack_id : any
            Key used in dictionary that stores stacks. Must be a valid key in a
            Python dict
        element : any
            Element to insert into stack, Can be any Python object.
        """
        # Make space if required

    def add_stack(
            self, stack_id, input_data=[], initial_capacity=len(input_data)
            ):
        """Add a stack to the MultiStack object

        Added as rightmost stack in main_array

        Parameters
        ----------
        stack_id : any
            Key used in dictionary that stores stacks. Must be a valid key in a
            Python dict
        input_data : list
            List of elements to add to stack, with rightmost element being at
            top of stack
        initial_capacity : int
            Initial num of elements in main_array to allocate to this stack
        """
        # Validate initial size given
        if initial_capacity < len(input_data):
            initial_capacity = len(input_data)

        self._ensure_space_is_allocated(initial_capacity)

        # Create empty stack
        if self.last_stack is None:
            self.stacks[stack_id] = StackInfo(
                0, starting_length=initial_capacity
            )
        else:
            self.stacks[stack_id] = StackInfo(
                self.last_stack.end_of_capacity_index + 1,
                starting_length=initial_capacity
            )
        # Update last_stack
        # Possible this pointer doesn't update when StackInfo object does;
        # however custom classes in Python are mutable by default, so shouldn't
        # be an issue
        self.last_stack = self.stacks[stack_id]

        # Insert elements into stack
        for element in input_data:
            self._add_element(stack_id, element)
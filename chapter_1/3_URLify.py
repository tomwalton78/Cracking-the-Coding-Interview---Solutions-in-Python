import unittest


def URLify(input_string):
    """Replace spaces in input_string with '%20', without using the
    replace() method of Python str objects, and must be done in-place.

    List slicing in Python is O(k), where k is the slice size, so this solution
    could be more optimal.

    Parameters
    ----------
    input_string : str
        String to process

    Returns
    -------
    str
        input_string, with spaces replaces by '%20'
    """
    # Convert to char array
    chars = list(input_string)

    # Get indices of spaces
    space_indices = []
    for i, char in enumerate(chars):
        if char == ' ':
            space_indices.append(i)

    # Extend char array to correct size
    chars.extend([None] * len(space_indices) * 2)

    # Replace spaces with '%20'
    for i, index in enumerate(space_indices):
        adjusted_index = index + (i * 2)  # * 2, since adding 2 chars each loop
        str_end_index = len(input_string) + (i * 2) - 1

        chars[adjusted_index: str_end_index + 2 + 1] = (
            list('%20') + chars[adjusted_index + 1: str_end_index + 1]
        )

    return ''.join(chars)


def URLify_solution(input_string):
    """Same goal as URLify, but using more efficient solution from book.

    Same input and output as URLify.
    """
    # First, count number of spaces in string
    space_count = 0
    for char in input_string:
        if char == ' ':
            space_count += 1

    # Check that there are spaces
    if space_count == 0:
        return input_string

    # Turn input_string into char array, with extra space for the chars we will
    # add
    chars = list(input_string) + [None] * space_count * 2

    # Get index of last element in chars, which represents highest unused index
    # in chars array
    index = len(chars) - 1
    # Iterate through indices of original input_string, backwards
    for i in range(len(input_string) - 1, -1, -1):
        # If char is a space, insert '%20' into highest unused (not None) at
        # back of chars array
        if chars[i] == ' ':
            chars[index - 2: index + 1] = '%20'
            # Update highest unused index at back of chars array
            index -= 3

        # If char is not a space, insert char value into highest unused (not
        # None) at back of chars array
        else:
            chars[index] = chars[i]
            # Update highest unused index at back of chars array
            index -= 1

    return ''.join(chars)


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        ('the quick brown fox', 'the%20quick%20brown%20fox'),
        ('Python', 'Python'),
        ('python  programmer', 'python%20%20programmer'),
    ]

    def test_URLify(self):
        for test_input, test_output in self.data:
            self.assertEqual(URLify(test_input), test_output)

    def test_URLify_solution(self):
        for test_input, test_output in self.data:
            self.assertEqual(URLify(test_input), test_output)


if __name__ == '__main__':

    unittest.main()

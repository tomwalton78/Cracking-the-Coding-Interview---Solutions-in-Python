import unittest

from data_structures.arrays_and_strings.array_sorting import quick_sort


def is_unique(input_string):
    """Find out if input_string has all unique characters, or not.

    Parameters
    ----------
    input_string : str
        String to check for uniqueness

    Returns
    -------
    bool
        True if string is unique, False otherwise
    """
    # Initialise dict to contain characters that have already been discovered
    # in string
    chars_found = {}

    # Iterate through string to check each char to see if it has been found
    # before in string
    for char in input_string:
        try:
            # Attempt to access key in hash table, to check if it has already
            # been found
            chars_found[char]
            return False

        except KeyError:
            # Store char as found
            chars_found[char] = True

    # Can only determine if string has all unique chars after checking entire
    # string
    return True


def is_unique_v2(input_string):
    """Find out if input_string has all unique characters, or not.

    Cannot use additional data structures (constraint of problem), therefore
    sorts array, then checks for duplicate adjacent elements.

    Parameters
    ----------
    input_string : str
        String to check for uniqueness

    Returns
    -------
    bool
        True if string is unique, False otherwise
    """
    # Handle special case of empty string
    if len(input_string) == 0:
        return True

    sorted_input_string = ''.join(quick_sort(list(input_string)))

    # Iterate through chars in sorted string, checking for duplicate adjacent
    # chars
    for i, char in enumerate(sorted_input_string[:-1]):
        # Compare elements i and i+1
        if char == sorted_input_string[i+1]:
            return False

    return True


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        ('golfer', True),
        ('golfer GO', True),  # check case sensitivity
        ('python programmer', False),
        ('', True),
        ('  ', False)
    ]

    def test_is_unique(self):
        for test_input, test_output in self.data:
            self.assertEqual(is_unique(test_input), test_output)

    def test_is_unique_v2(self):
        for test_input, test_output in self.data:
            self.assertEqual(is_unique_v2(test_input), test_output)


if __name__ == '__main__':

    unittest.main()

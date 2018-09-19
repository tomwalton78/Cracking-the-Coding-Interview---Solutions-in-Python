import unittest


def value_counts(input_string):
    """Computes count of each unique char in input_string

    Parameters
    ----------
    input_string : str
        String to process

    Returns
    -------
    val_counts : dict
        Keys are each unique char in input_string; values are counts of char in
        input_string
    """
    val_counts = {}
    for char in input_string:
        if char in val_counts:
            val_counts[char] += 1
        else:
            val_counts[char] = 0

    return val_counts


def is_permutation(str_1, str_2):
    """Checks to see if str_1 is a permutation of str_2.

    Permutation is taken to mean same as anagram.

    Parameters
    ----------
    str_1 : str
        First string in comparison
    str_2 : str
        Second string in comparison

    Returns
    -------
    bool
        True if str_1 is permutation of str_2, False otherwise
    """
    # First check that string lengths match
    if len(str_1) != len(str_2):
        return False

    # Compute value counts on both strings
    str_1_val_counts = value_counts(str_1)
    str_2_val_counts = value_counts(str_2)

    # Check for identical value counts
    if str_1_val_counts == str_2_val_counts:
        return True
    else:
        return False


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        (('python', 'pythonn'), False),  # check unequal lengths
        (('python', 'thonpy'), True),
        (('thonpy', 'Thonpy'), False),  # check case sensitivity
        (('python', 'noptyu'), False),
        (('silent', 'listen'), True)
    ]

    def test_is_permutation(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                is_permutation(test_input[0], test_input[1]), test_output
            )


if __name__ == '__main__':

    unittest.main()

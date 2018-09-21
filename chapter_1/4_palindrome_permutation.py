import unittest


def is_palindrome_permutation(input_string):
    """Checks to see if input_string is a permutation of a palindrome

    Using bool (is even?) instead of int value reduces space usage.

    Parameters
    ----------
    input_string : str
        String to check

    Returns
    -------
    bool
        True if input_string is a palindrome permutation, False otherwise
    """
    # Generate is even counts hash table
    char_counts_is_even = {}
    for char in input_string:
        if char not in char_counts_is_even:
            char_counts_is_even[char] = False
        else:
            # if True (even count), swithc it to False (odd count)
            if char_counts_is_even[char]:
                char_counts_is_even[char] = False
            # if False switch to True
            else:
                char_counts_is_even[char] = True

    # Check is even counts are mostly even (allow up to 1 odd count)
    num_odd_counts = 0  # keep track of how many counts are odd
    for key, is_char_count_even in char_counts_is_even.items():
        # Check to see if count is odd
        if not is_char_count_even:
            num_odd_counts += 1
        # Check not too many odds
        if num_odd_counts > 1:
            return False

    return True


def is_palindrome_permutation_solution(input_string):
    """Same goal as is_palindrome_permutation, but using more efficient
    solution from book, using a bit vector.
    """
    bit_vector = create_bit_vector(input_string)
    # bit_vector must be all 0s, or just have 1 bit set (to 1)
    return bit_vector == 0 or is_exactly_one_bit_set(bit_vector)


def create_bit_vector(input_string):
    """Creates a bit vector to represent all chars possible in the input
    string, set to 1 if the char occurs an odd no. of times in the input
    string.

    Parameters
    ----------
    input_string : str
        String to process

    Returns
    -------
    bit_vector : int
        Bit vector representing the chars and which ones have odd counts in
        input_string
    """
    # Initialise bit vector
    bit_vector = 0
    for char in input_string:
        # Get unicode no. that represents char
        index = ord(char)
        # Update bit vector at this index
        bit_vector = toggle(bit_vector, index)

    return bit_vector


def toggle(bit_vector, index):
    """Toggle bit at index in bit vector

    Parameters
    ----------
    bit_vector : int
        Bit vector to toggle
    index : int
        Index of bit to toggle in bit vector
    """
    # Validate index
    if index < 0:
        # i.e. no change is applied
        return bit_vector

    # Create number with 1 in index place (index digits from right, in binary),
    # 0s everywhere else
    mask = 1 << index
    # check if bit we are togglingin bit vector is off (0)
    if (bit_vector & mask) == 0:
        # Turn bit on
        bit_vector |= mask
    else:
        # Turn bit off
        bit_vector &= ~mask

    return bit_vector


def is_exactly_one_bit_set(bit_vector):
    """Check that only 1 bit is set (==1), and all others are 0

    Works by subtracting one from bit_vector (e.g. 00100100 -> 00100011). Then,
    if only 1 bit is set to 1 (i.e. just bit 2 places from right end), ANDing
    the result with the bit_vector should give 0s.

    Parameters
    ----------
    bit_vector : int
        Bit vector to check

    Returns
    -------
    bool
        True if exactly 1 bit is set; False otherwise
    """
    return (bit_vector & (bit_vector - 1)) == 0


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs
    data = [
        ('palinnilap', True),
        ('paalinnipl', True),
        ('paalinnipll',  True),
        ('paliinp',  False),
        ('amanaplanacanalpanama', True)
    ]

    def test_is_palindrome_permutation(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                is_palindrome_permutation(test_input), test_output
            )

    def test_is_palindrome_permutation_solution(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                is_palindrome_permutation_solution(test_input), test_output
            )


if __name__ == '__main__':

    unittest.main()

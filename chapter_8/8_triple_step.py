import unittest


def triple_step(n):
    """For a child running up a staircase with n steps, and the child can hop
    either 1, 2 or 3 steps at a time, count how many possible ways the child
    can run up the steps.

    Trick is to recognise that answer is sum of no. of ways at (n-1), (n-2) and
    (n-3) steps. Imagine that you are about to do the first hop. If you hop 1
    step, you must then go down the (n-1) no. of ways route, if you hop 2 steps
    you must go down the (n-2) route, and if you hop 3 steps you must go down
    the (n-3) route.

    Parameters
    ----------
    n : int
        No. of steps in staircase

    Returns
    -------
    int
        No. of possible ways child can run up steps
    """
    # Initialise cache array with empty values
    cache_arr = [None for i in range(n)]

    # Populate cache array with first 3 values
    cache_arr[0:3] = [1, 1, 2]

    # Populate cache array up to n-1
    for i in range(3, n):
        cache_arr[i] = cache_arr[i-1] + cache_arr[i-2] + cache_arr[i-3]

    if n > 2:
        # Return sum of last 3 elements in cache array
        return sum(cache_arr[-3:])
    else:
        # Return nth element of cache array
        return cache_arr[n]


class Test(unittest.TestCase):
    """Test cases"""
    # Define test case inputs, and expected outputs

    data = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
    ]

    def test_triple_step(self):
        for test_input, test_output in self.data:
            self.assertEqual(
                triple_step(test_input), test_output
            )


if __name__ == '__main__':

    unittest.main()

# https://www.codewars.com/kata/find-the-odd-int/


def find_it(seq):
    """
    Given an array, find the int that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.

    :param seq: list of integers
    :return: int that appears an odd number of times
    """
    d = {}
    while len(seq) > 0:
        m = min(seq)
        d[m] = 0
        while m in seq:
            d[m] += 1
            seq.remove(m)
    for x in d:
        if d[x] % 2 != 0:
            return x


assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
assert find_it([1,3,4,2,1,2,4,3,4,3,4]) == 3
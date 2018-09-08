# https://www.codewars.com/kata/sum-of-pairs/


def sum_pairs(ints, s):
    """
    Given a list of integers and a single sum value, return the first two values (parse from the left please)
    in order of appearance that add up to form the sum.

    :param ints: list
    :param s: sum
    :return: the sum of the first two values equal value "s"
    """
    alreadyseen = {}
    for i in range(len(ints)):
        tst = s - ints[i]
        if tst in alreadyseen:
            return [tst, ints[i]]
        alreadyseen[ints[i]] = True
    return None


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
assert sum_pairs(l1, 8) == [1, 7]
assert sum_pairs(l2, -6) == [0, -6]
assert sum_pairs(l3, -7) is None
assert sum_pairs(l4, 2) == [1, 1]
assert sum_pairs(l5, 10) == [3, 7]
assert sum_pairs(l6, 8) == [4, 4]
assert sum_pairs(l7, 0) == [0, 0]
assert sum_pairs(l8, 10) == [13, -3]

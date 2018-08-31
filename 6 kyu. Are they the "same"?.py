# https://www.codewars.com/kata/are-they-the-same/


def comp(array1, array2):
    """
    checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that
    the elements in b are the elements in a squared, regardless of the order.
    :return: True if arrays is the "same"
    """
    for x in array1:
        if x ** 2 in array2:
            array2.remove(x ** 2)
    return array2 == []


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a, b) is True
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
assert comp(a, b) is False
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
assert comp(a, b) is False

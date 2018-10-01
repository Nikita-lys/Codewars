# https://www.codewars.com/kata/build-tower/


def tower_builder(n):
    """
    Build Tower

    Build Tower by the following given argument:
    number of floors (integer and always greater than 0).

    Tower block is represented as *

    Python: return a list;
    Have fun!
    :param n: n floors
    :return: tower
    """
    res = []
    len = n + n - 1
    for i in range(n):
        res.append((' ' * i) + ('*' * len) + (' ' * i))
        len -= 2
    return res[::-1]


assert tower_builder(6) == ['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********']

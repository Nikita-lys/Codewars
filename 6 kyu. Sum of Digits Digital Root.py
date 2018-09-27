# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/


def digital_root(n):
    """
    n this kata, you must create a digital root function.

    A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
    If that value has two digits, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.

    digital_root(942)
    => 9 + 4 + 2
    => 15 ...
    => 1 + 5
    => 6

    :param n: number
    :return: sum of the digits of n
    """
    if len(str(n)) < 2:
        return n
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return digital_root(res)


assert digital_root(16) == 7
assert digital_root(456) == 6
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2
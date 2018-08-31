# https://www.codewars.com/kata/does-my-number-look-big-in-this/

def narcissistic(n):
    # return value == sum(int(x) ** len(str(value)) for x in str(value))
    """
    A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number
    of digits.
        For example, take 153 (3 digits):
        1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

    :param n: Digit
    :return: True if Digit is Narcissistic Number
    """
    sum = 0
    for x in str(n):
        sum += int(x) ** len(str(n))
    return sum == n


assert narcissistic(7) is True
assert narcissistic(371) is True
assert narcissistic(122) is False
assert narcissistic(4887) is False
assert narcissistic(92727) is True
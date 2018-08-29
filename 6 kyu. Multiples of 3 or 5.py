# https://www.codewars.com/kata/multiples-of-3-or-5

def solution(n):
    """
    returns the sum of all the multiples of 3 or 5 below the number passed in
    :param n: number
    :return: sum
    """
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


assert solution(10) == 23
assert solution(4) == 3
assert solution(3) == 0
# https://www.codewars.com/kata/primes-in-numbers

# Не прошёл тест:
# Time: 1675ms Passed: 0 Failed: 1 Exit Code: 1
# Test Results:
# '(17)(2**2)(3**3)(5)(7)(11**2)' should equal '(2**2)(3**3)(5)(7)(11**2)(17)'


def primeFactors(n):
    """
    Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string
    with the following form :
    "(p1**n1)(p2**n2)...(pk**nk)"

    :param n: number
    :return: string likes "(p1**n1)(p2**n2)...(pk**nk)"
    """
    d = {}
    for i in range(2, n + 1):
        while n % i == 0 and n >= 1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            n /= i
    res = ''
    for x in d:
        if d[x] > 1:
            res += '(' + str(x) + '**' + str(d[x]) + ')'
        else:
            res += '(' + str(x) + ')'
    return res


assert primeFactors(7775460) == '(2**2)(3**3)(5)(7)(11**2)(17)'
assert primeFactors(86240) == '(2**5)(5)(7**2)(11)'
print(primeFactors(7775460))
print(primeFactors(86240))

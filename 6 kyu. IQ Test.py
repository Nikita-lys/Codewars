# https://www.codewars.com/kata/iq-test/


def iq_test(numbers):
    """
    Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given
    numbers differs from the others. Bob observed that one number usually differs from the others in evenness.
    Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different
    in evenness, and return a position of this number.
    ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements
    start from 1 (not 0)

    iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
    iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

    :return: index of number that is different in evenness
    """
    evenodd, indeven, indodd = 0, 0, 0
    index = 1
    for x in numbers.split():
        if int(x) % 2 == 0:
            evenodd += 1
            indeven = index
        elif int(x) % 2 != 0:
            evenodd -= 1
            indodd = index
        index += 1
    if evenodd > 0:
        return indodd
    elif evenodd < 0:
        return indeven


assert iq_test("2 4 7 8 10") == 3
assert iq_test("1 2 1 1") == 2

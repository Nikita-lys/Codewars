# https://www.codewars.com/kata/counting-duplicates/


def duplicate_count(text):
    """
    Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
    digits that occur more than once in the input string. The input string can be assumed to contain only alphabets
    (both uppercase and lowercase) and numeric digits.

    :param text: string
    :return: count of dublicates
    """
    d = {}
    for x in text.lower():
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    count = 0
    for x in d:
        if d[x] > 1:
            count += 1
    return count


assert duplicate_count("abcde") == 0
assert duplicate_count("abcdea") == 1
assert duplicate_count("indivisibility") == 1
assert duplicate_count("aA11") == 2

# https://www.codewars.com/kata/count-characters-in-your-string/


def count(string):
    """
    The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba
    then the result should be { 'a': 2, 'b': 1 }

    What if the string is empty ? Then the result should be empty object literal { }
    :param string:
    :return: dictionary
    """
    d = {}
    for x in string:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d


assert count('aba') == {'a': 2, 'b': 1}
assert count('') == {}
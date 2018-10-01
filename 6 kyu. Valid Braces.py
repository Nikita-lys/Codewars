# https://www.codewars.com/kata/valid-braces/


def validBraces(string):
    """
    Write a function that takes a string of braces, and determines if the order of the braces is valid.
    It should return true if the string is valid, and false if it's invalid.

    This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
    Thanks to @arnedag for the idea!

    All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

    What is considered Valid?

    A string of braces is considered valid if all braces are matched with the correct brace.

    Examples

    "(){}[]"   =>  True
    "([{}])"   =>  True
    "(}"       =>  False
    "[(])"     =>  False
    "[({})](]" =>  False

    :param string: brackets
    :return: is string valid return True else return False
    """
    stack = []
    for x in string:
        if x == '(' or x == '{' or x == '[':
            stack.append(x)
        else:
            try:
                if x == ')':
                    if stack.pop() == '(':
                        continue
                    else:
                        return False
                elif x == '}':
                    if stack.pop() == '{':
                        continue
                    else:
                        return False
                elif x == ']':
                    if stack.pop() == '[':
                        continue
                    else:
                        return False
            except IndexError:
                return False
    return stack != ''


assert validBraces("(){}[]") is True
assert validBraces("([{}])") is True
assert validBraces("(}") is False
assert validBraces("[(])") is False
assert validBraces("[({})](]") is False
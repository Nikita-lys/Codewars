# https://www.codewars.com/kata/stop-gninnips-my-sdrow/


def spin_words(sentence):
    """
    Write a function that takes in a string of one or more words, and returns the same string, but with all five
    or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only
    letters and spaces. Spaces will be included only when more than one word is present.

    :param sentence: string
    :return: string with reversed words 
    """
    res = ''
    for x in sentence.split():
        if len(x) > 4:
            res += x[::-1] + ' '
        else:
            res += x + ' '
    return res.strip()


assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert spin_words("This is a test") == "This is a test"
assert spin_words("This is another test") == "This is rehtona test"
assert spin_words("Welcome") == "emocleW"

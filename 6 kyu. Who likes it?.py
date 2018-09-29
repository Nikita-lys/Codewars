# https://www.codewars.com/kata/who-likes-it/


def likes(names):
    """
    You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or
    other items. We want to create the text that should be displayed next to such an item.

    Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
    like an item. It must return the display text as shown in the examples:

    :param names:
    :return:
    """
    res = ''
    if len(names) > 1:
        if len(names) > 3:
            return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
        for x in names:
            if x == names[len(names) - 1]:
                return res[:len(res) - 2] + ' and ' + x + ' like this'
            else:
                res += x + ', '
    else:
        return names[0] + ' likes this' if len(names) > 0 else 'no one likes this'


assert likes([]) == 'no one likes this'
assert likes(['Peter']) == 'Peter likes this'
assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'

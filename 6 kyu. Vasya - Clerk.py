# https://www.codewars.com/kata/vasya-clerk/

# не проходит 1 тест


def tickets(people):
    """
    The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in
    a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

    Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

    Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets
    strictly in the order people follow in the line?

    Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that
    moment. Otherwise return NO.

    :param people: people's money
    :return: YES or NO
    """
    d = {25 : 0, 50 : 0, 100 : 0}
    for x in people:
        if x == 25:
            d[x] += 1
        elif x == 50:
            if d[25] > 0:
                d[25] -= 1
                d[x] += 1
            else:
                return 'NO'
        elif x == 100:
            if d[25] > 0 and d[50] > 0:
                d[25] -= 1
                d[50] -= 1
                d[x] += 1
            elif d[25] > 2:
                d[25] -= 3
            else:
                return 'NO'
    return 'YES'


print(tickets([25, 25, 25, 100]))
print(tickets([25,25,75,25,25,50,50,50,50]))

assert tickets([25, 25, 50]) == 'YES'
assert tickets([25, 100]) == 'NO'
assert tickets([25, 25, 50, 50, 100]) == 'NO'

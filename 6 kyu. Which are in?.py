# https://www.codewars.com/kata/which-are-in/

# Не прошёл тесты. Не могу понять почему


def in_array(a1, a2):
    d = {}
    for x in sorted(a1):
        d[x] = 0
        for y in a2:
            if x in y:
                d[x] += 1
    res = []
    for x in d:
        if d[x] > 0:
            res.append(x)
    return res


a1 = ["arp", "strong", "live"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

assert in_array(a1, a2) == r
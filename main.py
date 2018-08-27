import test

# 1
def unique_in_order(iterable):
    """
    Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
    elements with the same value next to each other and preserving the original order of elements.
    """
    # list = []
    # prev = None
    if not iterable:
        return []
    list = [iterable[0]]
    prev = iterable[0]
    for x in iterable:
        if x != prev:
            list += [x]
        prev = x
    return list


assert unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B']
assert unique_in_order([]) == []
assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
assert unique_in_order([1,2,2,3,3]) == [1,2,3]


# 2
def remove(s, n):
    """
    Remove n exclamation marks in the sentence from left to right. n is positive integer.

    :param s: string
    :param n: count exclamation marks
    :return: string without n exclamation marks
    """
    while n > 0:
        if '!' in s:
            c = s.find('!')
            s = s[:c] + s[c+1:]
            n -= 1
        else:
            break
    return s


assert remove("Hi!", 1) == "Hi"
assert remove("Hi!", 100) == "Hi"
assert remove("Hi!!!", 1) == "Hi!!"
assert remove("Hi!!!", 100) == "Hi"
assert remove("!Hi", 1) == "Hi"
assert remove("!Hi!", 1) == "Hi!"
assert remove("!Hi", 100) == "Hi"
assert remove("!!!Hi !!hi!!! !hi", 1) == "!!Hi !!hi!!! !hi"
assert remove("!!!Hi !!hi!!! !hi", 3) == "Hi !!hi!!! !hi"
assert remove("!!!Hi !!hi!!! !hi", 100) == "Hi hi hi"


# 3
def countBits(x):
    # return bin(n).count("1")
    """
    Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one
    in the binary representation of that number.

    :param x: integer
    :return: number of bits that are equal to one in the binary representation of that number
    """
    n, res = "", 0
    while x > 0:
        y = str(x % 2)
        res += 1 if y == '1' else 0
        n = y + n
        x = int(x / 2)
    return res


assert countBits(0) == 0
assert countBits(4) == 1
assert countBits(7) == 3
assert countBits(9) == 2
assert countBits(10) == 2


# 4
def tribonacci(signature, n):
    # for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    #     return s[:n]
    """
    Like Fibonacci, but this is Tribonacci
    [1, 1, 1] -> [1, 1 ,1, 3, 5, 9, 17, 31, ...]

    :param signature: the first three numbers of Tribonacci sequence
    :param n: count of numbers
    :return: n numbers Tribonacci sequence
    """
    if n < 4:
        return [] if n == 0 else [signature[0]] if n == 1 else [signature[0], signature[1]] if n == 2 else signature
    cur = 3
    while n - 3 > 0:
        signature.append(signature[cur-3] + signature[cur-2] + signature[cur-1])
        cur += 1
        n -= 1
    return signature


assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
assert tribonacci([1, 1, 1], 1) == [1]
assert tribonacci([300, 200, 100], 0) == []
assert tribonacci([0.5, 0.5, 0.5], 30) == [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5,
                                           600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5,
                                           144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5,
                                           10301680.5]

# 5
def move_zeros(array):
    # 1. return sorted(array, key=lambda x: x==0 and type(x) is not bool)
    # 2. l = [i for i in arr if isinstance(i, bool) or i!=0]
    #     return l+[0]*(len(arr)-len(l))
    """
    Algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    :param array: seq
    :return: seq where zero in the end
    """
    n, i, same = 0, 0, array.copy()
    for x in array:
        if x == 0 and type(x) is not bool:
            del same[i]
            n += 1
            i -= 1
        i += 1
    same += [0] * n
    return same


assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,
                                                                         0]
assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,
                                                                                          1,3,[],1,9,{},9,0,0,0,0,0,0,
                                                                                          0,0,0,0]
assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
assert move_zeros(["a","b"]) == ["a","b"]
assert move_zeros(["a"]) == ["a"]
assert move_zeros([0,0]) == [0,0]
assert move_zeros([0]) == [0]
assert move_zeros([]) == []


# 6 Mumbling
def accum(s):
    res = ''
    i = 0
    for x in s:
        res += x.upper() + x.lower() * i + '-'
        i += 1
    return res[:len(res) - 1]


assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
assert accum("NyffsGeyylB") == "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
assert accum("MjtkuBovqrU") == "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
assert accum("EvidjUnokmM") == "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
assert accum("HbideVbxncC") == "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"


# accum("abcd")  # "A-Bb-Ccc-Dddd"
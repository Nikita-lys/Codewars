# https://www.codewars.com/kata/snail

# Не уложился по времени :)

def snail(a):
    """
    Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling
    clockwise.

    array = [[1,2,3],
            [4,5,6],
         [  7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]

    :param a: array
    :return: array elements arranged from outermost elements to the middle element
    """

    res = []
    n = len(a[0])   # количество строк или столбцов
    full = n        # количество заполнений в одном направлении

    for k in range(n):  # обход первой строки
        res.append(a[0][k])  # [1, 2, 3]
        a[0][k] = -1

    countfull = 1   # счётчик заполнений
    x = n
    i, j = 0, n - 1
    while x < n * n - 1:
        # go down
        if a[i][j] == -1 and a[i+1][j] != -1:
            countfull += 1
            if countfull == 2:
                full -= 1
                countfull = 0
            for down in range(i + 1, i + full + 1):
                res.append(a[down][j])
                a[down][j] = -1
                i += 1
                x += 1

        # go left
        if a[i][j] == -1 and a[i][j - 1] != -1:
            countfull += 1
            if countfull == 2:
                full -= 1
                countfull = 0
            for left in range(i - 1, j - full - 1, -1):
                res.append(a[i][left])
                a[i][left] = -1
                j -= 1
                x += 1

        # go up
        if a[i][j] == -1 and a[i - 1][j] != -1:
            countfull += 1
            if countfull == 2:
                full -= 1
                countfull = 0
            for up in range(i - 1, i - full - 1, -1):
                res.append(a[up][j])
                a[up][j] = -1
                i -= 1
                x += 1

        # go right
        if a[i][j] == -1 and a[i][j + 1] != -1:
            countfull += 1
            if countfull == 2:
                full -= 1
                countfull = 0
            for right in range(j + 1, j + full + 1):
                res.append(a[i][right])
                a[i][right] = -1
                j += 1
                x += 1

    return res or []


array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]

array2 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array3 = [[]]

print(snail(array))

def count_smileys(arr):
    """
    Given an array (arr) as an argument complete the function countSmileys that should return the total number of
    smiling faces.

    Valid smiley face examples:
    :) :D ;-D :~)
    Invalid smiley faces:
    ;( :> :} :]
    :param arr: smiling faces
    :return: total number of smiling faces
    """

    res = 0
    for x in arr:
        if x[0] == ':' or x[0] == ';':
            if x[1] == '-' or x[1] == '~':
                if x[2] == 'D' or x[2] == ')':
                    res += 1
            elif x[1] == 'D' or x[1] == ')':
                res += 1
    return res


assert count_smileys([]) == 0
assert count_smileys([':D',':~)',';~D',':)']) == 4
assert count_smileys([':)',':(',':D',':O',':;']) == 2
assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1
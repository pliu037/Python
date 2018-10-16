"""
https://projecteuler.net/problem=116
https://projecteuler.net/problem=117
"""


def get_combination_memo(length, sizes):
    """

    """
    combination_memo = [1]
    for i in xrange(1, length + 1):
        total = 0
        for size in sizes:
            look_back = i - size
            if look_back >= 0:
                total += combination_memo[look_back]
        look_back = i - 1
        if look_back >= 0:
            total += combination_memo[look_back]
        combination_memo.append(total)
    return combination_memo


def get_single_combinations(length, sizes):
    """

    """
    total = 0
    for size in sizes:
        total += get_combination_memo(length, [size])[length] - 1
    return total


print get_single_combinations(50, [2, 3, 4])
length = 50
print get_combination_memo(length, [2, 3, 4])[length]

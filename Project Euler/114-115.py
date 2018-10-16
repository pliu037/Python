"""
https://projecteuler.net/problem=114
https://projecteuler.net/problem=115
"""


def get_next_combination(memo, index, min_size):
    """

    """
    total = memo[index - 1]
    check = index - min_size
    if check >= 0:
        total += 1
    for i in xrange(check):
        total += memo[i]
    return total


def get_combination_memo(length, min_size):
    """

    """
    combination_memo = [1 for _i in xrange(min_size)]
    for i in xrange(length - min_size + 1):
        combination_memo.append(get_next_combination(combination_memo, i + min_size, min_size))
    return combination_memo


def get_min_length_for_target_combinations(target, min_size):
    """

    """
    combination_memo = [1 for _i in xrange(min_size)]
    index = min_size
    while combination_memo[-1] <= target:
        combination_memo.append(get_next_combination(combination_memo, index, min_size))
        index += 1
    return len(combination_memo) - 1


length = 50
print get_combination_memo(length, 3)[-1]
print get_min_length_for_target_combinations(1000000, 50)

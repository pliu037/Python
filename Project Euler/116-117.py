"""
https://projecteuler.net/problem=116
https://projecteuler.net/problem=117
"""


def get_combination_memo(length, sizes):
    """
    Given a list of block sizes, <sizes>, generates a list of combination counts of length <length + 1> where
    the index is the sequence length
    """
    combination_memo = [1]
    for i in xrange(1, length + 1):
        total = 0

        # If the position at index is unfilled, then there are memo[index - 1] combinations
        look_back = i - 1
        if look_back >= 0:
            total += combination_memo[look_back]

        '''
        If <index> is the start of a block, for all block sizes, then <index - [block size]> is the first
        position in which a new block could start (the above recursion captures that multiple unfilled squares
        can separate the blocks by accounting for solutions with an arbitrary prefix of unfilled squares)
        '''
        for size in sizes:
            look_back = i - size
            if look_back >= 0:
                total += combination_memo[look_back]

        combination_memo.append(total)
    return combination_memo


def get_single_combinations(length, sizes):
    """
    Given a list of block sizes, <sizes>, returns the sum of combination counts on a sequence of length
    <length> if block sizes cannot be mixed
    """
    total = 0
    for size in sizes:
        total += get_combination_memo(length, [size])[length] - 1
    return total


print get_single_combinations(50, [2, 3, 4])
print get_combination_memo(50, [2, 3, 4])[-1]

"""
https://projecteuler.net/problem=114
https://projecteuler.net/problem=115
"""


def get_next_combination(memo, index, min_size):
    """
    Given the memo of combinations up to <index - 1>, calculates the number of combinations for <index>
    """
    # If the position at index is black, then there are memo[index - 1] combinations
    total = memo[index - 1]

    '''
    If <index> is the start of a red block, for all valid red block sizes, then <index - [red block size] - 1>
    is the first position in which a new red block could start (there must be at least one black box between
    the red blocks; the above recursion captures that multiple black boxes can separate the red blocks by
    accounting for solutions with an arbitrary prefix of black boxes)
    '''
    check = index - min_size
    for i in xrange(check):
        total += memo[i]

    # The above loop assumes a red block terminating with at least one black box, but this doesn't account for
    # the case in which the red block covers the remaining squares
    if check >= 0:
        total += 1
    return total


def get_combination_memo(length, min_size):
    """
    Given <min_size> of a red block, generates a list of combination counts of length <length + 1> where the
    index is the sequence length
    """
    # For sequences of length less than <min_size>, the only solution is all black boxes
    combination_memo = [1 for _i in xrange(min_size)]
    for i in xrange(length - min_size + 1):
        combination_memo.append(get_next_combination(combination_memo, i + min_size, min_size))
    return combination_memo


def get_min_length_for_target_combinations(target, min_size):
    """
    Given <min_size> of a red block, returns the index for which the combination count first exceeds <target>
    """
    # For sequences of length less than <min_size>, the only solution is all black boxes
    combination_memo = [1 for _i in xrange(min_size)]
    index = min_size
    while combination_memo[-1] <= target:
        combination_memo.append(get_next_combination(combination_memo, index, min_size))
        index += 1
    return len(combination_memo) - 1


print get_combination_memo(50, 3)[-1]
print get_min_length_for_target_combinations(1000000, 50)

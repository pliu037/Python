# Given a number pad, return the strings that can be returned given n moves
# that move like a knight
# Given a number pad, return the number of strings that can be returned
# given n moves that move like a knight

"""
Attempted to write a function to compute the valid moves given any grid and movement
(dimension_1 and dimension_2 would be 1 and 2, interchangeably, in the case of moving
like a knight. Then with the valid moves, tried to generate all reachable strings before
being reminded that we just needed the count.
Had a bug in get_valid_moves (checked direction_1 * dimension_1 but not direction_1 *
dimension_2)
Completed the single-step implementation but did not have time to attempt the memoized
implementation
Analysis:
- Wasted time by trying to solve a more general problem (any grid and movement) instead
  of just hard-coding the valid moves for the specific grid and movement given
- Started solving the slightly harder problem of generating all reachable strings rather
  than just counting them
- Started coding with only a rough idea of the solution, splitting my attention between
  solving what state must be maintained and how to store that state (the structure is
  complicated enough to be cumbersome to handle in working memory)
- Nervousness, especially when I realized I may not be able to finish, hampered my
  ability to think clearly, exacerbating the above problem
"""


from collections import defaultdict


grid = [["0", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"],
        [None, "9", None]]

directions = (-1, 1)


def get_valid_moves(grid, dimension_1, dimension_2):
    valid_moves = {}
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            current_value = grid[x][y]
            if current_value is None:
                continue
            if current_value not in valid_moves:
                valid_moves[current_value] = set()
            for direction_1 in directions:
                for direction_2 in directions:

                    # Have to check both dimension_1 and dimension_2 along both axes
                    check_x = x + direction_1 * dimension_1
                    check_y = y + direction_2 * dimension_2
                    if 0 <= check_x < len(grid) and 0 <= check_y < len(grid[0]) \
                            and grid[check_x][check_y] is not None:
                        valid_moves[current_value].add(grid[check_x][check_y])
                    check_x = x + direction_1 * dimension_2
                    check_y = y + direction_2 * dimension_1
                    if 0 <= check_x < len(grid) and 0 <= check_y < len(grid[0]) \
                            and grid[check_x][check_y] is not None:
                        valid_moves[current_value].add(grid[check_x][check_y])
    return valid_moves


def get_reachable_strings(valid_moves, num_steps, start):
    if num_steps == 0:
        return [start]

    """
    Memoizes the strings that are reachable in n steps from any starting point
    <strings_from_n_steps>:
        <num_steps>:
            <start_position>: [list of strings reachable after n steps starting from
                               start_position]
    """
    strings_from_n_steps = {1: {key: {key + value for value in values}
                                for key, values in valid_moves.iteritems()}}
    steps_remaining = num_steps - 1

    while steps_remaining > 0:

        # Finds the set of longest memoized strings and a second set consisting of the
        # longest memoized strings such that, appended, they are constructable in n or
        # fewer steps
        step_sizes = sorted(strings_from_n_steps.keys(), reverse=True)
        largest_size_memoized_so_far = step_sizes[0]
        base_positions = strings_from_n_steps[largest_size_memoized_so_far]
        for step_size in step_sizes:
            if step_size <= steps_remaining:
                steps_remaining -= step_size
                memoized_strings = strings_from_n_steps[step_size]
                break

        # Appends the two sets of strings chosen above such that the end_position of the
        # string from first set is the start_position of the string from the second set
        new_memoized_strings = defaultdict(set)
        for start_position, strings in base_positions.iteritems():
            for string in strings:
                last_position = string[-1]
                for move in memoized_strings[last_position]:
                    new_memoized_strings[start_position].add((string + move[1:]))

        strings_from_n_steps[largest_size_memoized_so_far + step_size] = \
            new_memoized_strings

    return strings_from_n_steps[num_steps][start]


def get_reachable_strings_count(valid_moves, num_steps, start):
    if num_steps == 0:
        return 1

    """
    Memoizes the number of strings that are reachable in n steps from any starting
    point:
    <counts_from_n_steps>:
        <num_steps>:
            <start_position>:
                <end_position>: <number of strings reachable after n steps starting from
                                 start_position and ending at end_position>
    """
    counts_from_n_steps = {}
    counts_from_1_step = defaultdict(dict)
    for start_position, next_positions in valid_moves.iteritems():
        for end_position in next_positions:
            if end_position not in counts_from_1_step[start_position]:
                counts_from_1_step[start_position][end_position] = 0
            counts_from_1_step[start_position][end_position] += 1
    counts_from_n_steps[1] = counts_from_1_step

    moves_remaining = num_steps - 1

    while moves_remaining > 0:

        # Finds the counts associated with the most number of steps memoized so far and
        # a second set of counts associated with a number of steps such that together
        # they are still n or fewer steps
        step_sizes = sorted(counts_from_n_steps.keys(), reverse=True)
        largest_size_memoized_so_far = step_sizes[0]
        base_positions = counts_from_n_steps[largest_size_memoized_so_far]
        for step_size in step_sizes:
            if step_size <= moves_remaining:
                moves_remaining -= step_size
                memoized_counts = counts_from_n_steps[step_size]
                break

        # Finds the counts associated with the combined number of steps starting at
        # start_position of the first set of counts and ending at the end_position of
        # the second set of counts such that the end_position of the first set is the
        # start_position of the string from the second set
        # If there are x ways to get from A -> B and y ways to get from B -> C, there
        # are x * y ways to get from A -> C
        new_memoized_counts = defaultdict(dict)
        for start_position, end_position_counts in base_positions.iteritems():
            for end_position, base_count in end_position_counts.iteritems():
                for memoized_end_position, memoized_end_position_count in \
                        memoized_counts[end_position].iteritems():
                    if memoized_end_position not in new_memoized_counts[start_position]:
                        new_memoized_counts[start_position][memoized_end_position] = 0
                    new_memoized_counts[start_position][memoized_end_position] += \
                        base_count * memoized_end_position_count

        counts_from_n_steps[largest_size_memoized_so_far + step_size] = \
            new_memoized_counts

    return sum([count for count in counts_from_n_steps[num_steps][start].values()])


valid_moves = get_valid_moves(grid, 1, 2)
print valid_moves
reachable_strings = get_reachable_strings(valid_moves, 4, "2")
print reachable_strings
print get_reachable_strings(valid_moves, 1, "4")
print len(reachable_strings)
print get_reachable_strings_count(valid_moves, 4, "2")

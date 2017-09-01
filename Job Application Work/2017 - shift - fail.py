# Given a list of sorted, disjoint  intervals, represented as tuples, and another interval, return a list of sorted,
# disjoint tuples with the new interval added, merging any overlapping intervals

"""
Attempted to iterate through the existing intervals, keeping track of which existing intervals are spanned by the new
interval and merging them
Analysis:
- started coding without explicitly enumerating the cases, leading to thrashing as I bounced back and forth between
  cases in working memory
"""


def merge_interval(intervals, new_interval):
    merged_interval_start = None
    merged_interval_open = False
    ret_intervals = []

    # new_interval starts after the last interval
    if new_interval[0] > intervals[-1][1]:
        return intervals + [new_interval]

    for index, interval in enumerate(intervals):
        if not merged_interval_open:

            # new_interval starts before or in the current interval
            # can only ever enter this section once
            if new_interval[0] <= interval[1]:

                # new_interval ends before the current interval
                if new_interval[1] < interval[0]:
                    ret_intervals.append(new_interval)
                    return ret_intervals + intervals[index:]

                # new_interval ends in the current interval
                elif new_interval[1] <= interval[1]:
                    ret_intervals.append((new_interval[0], max(interval[1], new_interval[1])))
                    return ret_intervals + intervals[index + 1:]

                # new_interval ends past the current interval
                else:
                    merged_interval_start = min(interval[0], new_interval[0])
                    merged_interval_open = True

            # new_interval starts after the current interval
            else:
                ret_intervals.append(interval)

        else:

            # new_interval ends before the current interval
            if new_interval[1] < interval[0]:
                ret_intervals.append((merged_interval_start, new_interval[1]))
                return ret_intervals + intervals[index:]

            # new_interval ends in the current interval
            elif new_interval[1] <= interval[1]:
                ret_intervals.append((merged_interval_start, max(interval[1], new_interval[1])))
                return ret_intervals + intervals[index + 1:]

    # new_interval ends after the final interval
    ret_intervals.append((merged_interval_start, new_interval[1]))
    return ret_intervals


print merge_interval([(3, 10), (13, 15)], (1, 2))
print merge_interval([(3, 10), (13, 15)], (1, 3))
print merge_interval([(3, 10), (13, 15)], (11, 12))
print merge_interval([(3, 10), (13, 15), (17, 20)], (10, 13))
print merge_interval([(3, 10), (13, 15), (17, 20)], (11, 17))
print merge_interval([(3, 10), (13, 15), (17, 20)], (10, 16))
print merge_interval([(3, 10), (13, 15)], (15, 20))

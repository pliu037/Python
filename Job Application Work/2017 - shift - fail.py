from heapq import heappush, heappop

# Given a list of sorted, disjoint  intervals, represented as tuples, and another interval, return a list of sorted,
# disjoint tuples with the new interval added, merging any overlapping intervals

"""
Attempted to iterate through the existing intervals, keeping track of which existing intervals are spanned by the new
interval and merging them
Analysis:
- started coding without explicitly enumerating the cases, leading to thrashing back and forth between cases in working
  memory
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
                    ret_intervals.append((min(interval[0], new_interval[0]), max(interval[1], new_interval[1])))
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


"""
Inspired by Christian Ohler's suggestion of treating intervals as points
We can perform a merge sort-like operation across many lists of intervals, subject to the constraint that each list
contains disjoint intervals in ascending order, coupled with a stack-based, parenthesis-matching-like operation
"""
OPEN = 0
CLOSE = 1


class Point:
    def __init__(self, value, flag, list_index):
        self.value = value
        self.flag = flag
        self.list_index = list_index

    # __cmp__ compares based on value and flag to ensure OPEN Points are popped off the heap first
    def __cmp__(self, other):
        return cmp((self.value, self.flag), (other.value, other.flag))


def merge_intervals(interval_lists):
    lengths = []
    pointers = []
    frontier_heap = []
    stack = []
    ret = []
    for i in xrange(len(interval_lists)):
        lengths.append(len(interval_lists[i]) * 2)
        heappush(frontier_heap, Point(interval_lists[i][0][0], OPEN, i))
        pointers.append(1)

    while frontier_heap:
        p = heappop(frontier_heap)
        list_index = p.list_index
        pos = pointers[list_index]

        # As long as there is a value on the stack there is an open interval, so when the last value is popped off the
        # stack, we create an interval spanning the value popped off the stack (the earlier value in this
        # super-interval) and the value just pulled from the frontier (the value that closed this super-interval)
        # It is important that Points are pulled off the frontier not only in ascending order of value, but also with
        # OPEN Points coming before CLOSE Points to prevent unintentional closing of a super-interval at a given value
        # where there are both OPEN and CLOSE Points and, by chance, the CLOSE Points are pulled off the frontier first
        if p.flag == OPEN:
            stack.append(p.value)
        else:
            v = stack.pop()
            if not stack:
                ret.append((v, p.value))

        if pos < lengths[list_index]:
            heappush(frontier_heap, Point(interval_lists[list_index][pos/2][pos % 2], pos % 2, list_index))
            pointers[list_index] += 1

    return ret


print merge_interval([(3, 10), (13, 15)], (1, 2)), merge_intervals([[(3, 10), (13, 15)], [(1, 2)]])
print merge_interval([(3, 10), (13, 15)], (1, 3)), merge_intervals([[(3, 10), (13, 15)], [(1, 3)]])
print merge_interval([(3, 10), (13, 15)], (11, 12)), merge_intervals([[(3, 10)], [(11, 12), (13, 15)]])
print merge_interval([(3, 10), (13, 15)], (16, 20)), merge_intervals([[(3, 10)], [(13, 15)], [(16, 20)]])
print merge_interval([(3, 10), (13, 15), (17, 20)], (10, 13)), \
    merge_intervals([[(3, 10), (13, 15)], [(17, 20)], [(10, 13)]])
print merge_interval([(3, 10), (13, 15), (17, 20)], (11, 17)), \
    merge_intervals([[(3, 10), (13, 15), (17, 20)], [(11, 17)]])
print merge_interval([(3, 10), (13, 15), (17, 20)], (10, 16)), \
    merge_intervals([[(3, 10)], [(13, 15)], [(10, 16)], [(17, 20)]])
print merge_interval([(3, 10), (13, 15)], (15, 20)), merge_intervals([[(3, 10), (13, 15)], [(15, 20)]])
print merge_interval([(3, 10), (13, 15)], (4, 9)), merge_intervals([[(3, 10), (13, 15)], [(4, 9)]])


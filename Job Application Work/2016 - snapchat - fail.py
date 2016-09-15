# Given a k right-shifted, sorted array, find the smallest element in O(log n)

'''
Attempted to find k first and planned to use k in a modified binary search to find the smallest element
Failed to implement a function to find k
Analysis:
- started writing recursive code before completely flushing out the recursive substructure (e.g.: what each level must
  check and what is the subsequent level's responsibility)
- need more practice manipulating interval indices (e.g.: inclusive and exclusive, wrapping around); currently, too much
  trial and error
- confused finding the smallest element with binary search for a given element (finding k is equivalent to finding the
  smallest element)
'''

def find_smallest(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
       return min(array)

    midpoint = len(array)/2

    # If the midpoint is smaller than the final element, then the smallest element must be on the left side (midpoint
    # included), otherwise it is on the right side (same logic is used in find_shift)
    if array[midpoint] < array[-1]:
        return find_smallest(array[:midpoint + 1])
    else:
        return find_smallest(array[midpoint + 1:])


def find_shift(array, start, end):
    if start == end - 1:
        return start
    if end - start == 2:
        if array[start] <= array[start + 1]:
            return start
        return start + 1

    midpoint = (start + end)/2
    if array[midpoint] < array[-1]:
        return find_shift(array, start, midpoint + 1)
    else:
        return find_shift(array, midpoint + 1, end)


def helper_shifted_binary_search(target, array, shift):

    # The pattern for wrapping some point x in the interval [s, e] is (x + shift - s) % (e - s + 1) + s
    # len(array) + 1 is used to guarantee at least one pass of the recursive function (if new_range >***=*** range)
    return shifted_binary_search(shift, (len(array) + shift - 1) % len(array) + 1, target, array, len(array) + 1)


def shifted_binary_search(start, end, target, array, range):
    if start < end:
        new_range = end - start
        midpoint = (start + end) / 2

    # If start >= end, then the segment wraps and the midpoint and range must be calculated differently
    else:
        new_range = len(array) - start + end
        midpoint = (start + end + len(array)) / 2 % len(array)

    if array[midpoint] == target:
        return midpoint

    # If the element is in the array, segment length decreases monotonically over recursions. Equivalently, if segment
    # length increases (a result of supporting wrap around) or remains unchanged, then the element is not in the array.
    if new_range >= range:
        return None

    if array[midpoint] < target:
        return shifted_binary_search((midpoint + 1) % len(array), end, target, array, new_range)
    else:
        return shifted_binary_search(start, midpoint, target, array, new_range)


test = [6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 5]
target = 12
print 'Smallest value: ' + str(find_smallest(test))
shift = find_shift(test, 0, len(test))
print 'Shifted by: ' + str(shift)
print str(target) + ' at index: ' + str(helper_shifted_binary_search(target, test, shift))

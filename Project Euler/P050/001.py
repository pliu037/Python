# https://projecteuler.net/problem=1


def sum_of_multiples_below_threshold(a, b, threshold):
    occurrences_of_a = int((threshold - 1)/a)
    occurrences_of_b = int((threshold - 1)/b)
    occurrences_of_ab = int((threshold - 1)/(a*b))
    return occurrences_of_a*(a + occurrences_of_a*a)/2 + \
        occurrences_of_b*(b + occurrences_of_b*b)/2 - \
        occurrences_of_ab*(a*b + occurrences_of_ab*a*b)/2


print sum_of_multiples_below_threshold(3, 5, 1000)

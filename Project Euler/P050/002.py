# https://projecteuler.net/problem=2


def sum_even_fibonacci(threshold):
    even_fibonacci = 2
    prev_odd_fibonacci = 1
    total = 0
    # Every third Fibonacci number is even: convert it to a function
    # of the previous even Fibonacci number and the odd Fibonacci
    # number that comes before it
    while even_fibonacci <= threshold:
        total += even_fibonacci
        next_even_fibonacci = 3*even_fibonacci + 2*prev_odd_fibonacci
        prev_odd_fibonacci = 2*even_fibonacci + prev_odd_fibonacci
        even_fibonacci = next_even_fibonacci
    return total


print sum_even_fibonacci(4000000)

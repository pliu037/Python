from test_runner import *

path = './q1'
function_name = 'Fibonacci'


def all_tests(c, s):
    base_test(c, s)
    correctness_test(c, s)
    recursion_depth_test(c, s)
    timeout_test(c, s)


@test()
def base_test(c, s):
    f = c()
    check = f.get_nth_fibonacci(1)
    if check != 0:
        s.add_err('First Fibonacci number should be 0, got ' + str(check))


@test()
def correctness_test(c, s):
    f = c()
    check = f.get_nth_fibonacci(13)
    if check != 144:
        s.add_err('Thirteenth Fibonacci number should be 144, got ' + str(check))


@test()
def recursion_depth_test(c, s):
    f = c()
    try:
        f.get_nth_fibonacci(1000)
    except RuntimeError as e:
        s.add_err(e.message)


@test()
@timer
def timeout_test(c, s):
    f = c()
    for _i in xrange(1000):
        f.get_nth_fibonacci(40)


run_tests(path, function_name, all_tests)

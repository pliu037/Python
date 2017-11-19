from utils import *

path = '..\\q1'
function_name = 'Fibonacci'


def all_tests(c, s):
    test1(c, s)
    test2(c, s)
    print s.file_name, s.errors, s.timings


def test1(c, s):
    f = c()
    check = f.get_nth_fibonacci(1)
    if check != 0:
        s.add_err(test1.__name__, 'test1 failed: First Fibonacci number should be 0, got ' + check)


@timer()
def test2(c, s):
    f = c()
    for _i in xrange(100):
        f.get_nth_fibonacci(40)


run_tests(path, function_name, all_tests)

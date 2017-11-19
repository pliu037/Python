from test_runner import *

path = './q3'
function_name = 'find_number_of_repeats'


def all_tests(f, s):
    empty_outer_test(f, s)
    empty_inner_test(f, s)
    found_test(f, s)
    not_found_test(f, s)
    repetition_found_test(f, s)
    repetition_not_found_test(f, s)
    found_timer_test(f, s)
    not_found_timer_test(f, s)


def empty_outer_test(f, s):
    pass


def empty_inner_test(f, s):
    pass


def found_test(f, s):
    pass


def not_found_test(f, s):
    pass


def repetition_found_test(f, s):
    pass


def repetition_not_found_test(f, s):
    pass


@timer()
def found_timer_test(f, s):
    pass


@timer()
def not_found_timer_test(f, s):
    pass


run_tests(path, function_name, all_tests)

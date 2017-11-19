from test_runner import *

path = './q3'
function_name = 'find_number_of_repeats'


def all_tests(f, s):
    empty_substr_test(f, s)
    empty_s_test(f, s)
    found_test(f, s)
    not_found_test(f, s)
    repetition_found_test(f, s)
    repetition_not_found_test(f, s)
    found_timer_test(f, s)
    not_found_timer_test(f, s)


@test()
def empty_substr_test(f, s):
    check = f('', 'abc')
    if check != -1:
        s.add_err('There is no amount of repetition of an empty substring that allows another string to fit within it')


@test()
def empty_s_test(f, s):
    pass


@test()
def found_test(f, s):
    pass


@test()
def not_found_test(f, s):
    pass


@test()
def repetition_found_test(f, s):
    pass


@test()
def repetition_not_found_test(f, s):
    pass


@test()
@timer
def found_timer_test(f, s):
    pass


@test()
@timer
def not_found_timer_test(f, s):
    pass


run_tests(path, function_name, all_tests)

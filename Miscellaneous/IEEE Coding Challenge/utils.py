import os
from os import listdir
from os.path import isfile, join
import sys
from functools import wraps
import time
import signal

__all__ = ['run_tests', 'timer', 'Stats']


def run_tests(path, entity_name, test):
    files = _get_py_files(path)
    sys.path.append(os.path.abspath(path))
    for f in files:
        exec('from ' + f[:-3] + ' import ' + entity_name)
        s = Stats(f[:-3])
        test(locals()[entity_name], s)


def timer(seconds=10):
    def decorator(f):
        def _handle_timeout(signum, frame):
            raise _TimeoutError()

        @wraps(f)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                start = time.time()
                f(args[0], args[1])
            except _TimeoutError:
                args[1].add_err(f.__name__, 'Timed out after ' + str(seconds) + 's')
            else:
                args[1].add_timing(f.__name__, time.time() - start)
            finally:
                signal.alarm(0)

        return wrapper

    return decorator


class Stats:
    def __init__(self, file_name):
        self.file_name = file_name
        self.errors = {}
        self.timings = {}

    def add_err(self, test_name, msg):
        self.errors[test_name] = msg

    def add_timing(self, test_name, timing):
        self.timings[test_name] = timing


def _get_py_files(path):
    return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.py')]


class _TimeoutError(Exception):
    pass

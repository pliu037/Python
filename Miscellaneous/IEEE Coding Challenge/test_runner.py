import os
from os import listdir
from os.path import isfile, join
import sys
from functools import wraps
import time
import signal
import inspect

__all__ = ['run_tests', 'timer']


def run_tests(path, entity_name, test):
    files = _get_py_files(path)
    sys.path.append(os.path.abspath(path))
    for f in files:
        file_name = f[:-3]
        try:
            exec('from ' + file_name + ' import ' + entity_name)
            s = _Stats(file_name)
            test(locals()[entity_name], s)
            s.report()
        except Exception as e:
            print file_name, e.message


def timer(seconds=10):
    def decorator(f):
        def _handle_timeout(signum, frame):
            raise _TimeoutError()

        @wraps(f)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            s = args[1]
            try:
                start = time.time()
                f(args[0], s)
            except _TimeoutError:
                s.add_err('Timed out after ' + str(seconds) + 's', fn=f.__name__)
            else:
                s.add_timing(time.time() - start, fn=f.__name__)
            finally:
                signal.alarm(0)

        return wrapper

    return decorator


class _Stats:
    def __init__(self, file_name):
        self.file_name = file_name
        self.errors = {}
        self.timings = {}

    def add_err(self, msg, fn=None):
        self.errors[fn if fn else _get_func_name()] = msg

    def add_timing(self, timing, fn=None):
        self.timings[fn if fn else _get_func_name()] = timing

    def report(self):
        print self.file_name, self.errors, self.timings


class _TimeoutError(Exception):
    pass


def _get_py_files(path):
    return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.py')]


def _get_func_name():
    return inspect.stack()[2][3]

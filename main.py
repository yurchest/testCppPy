import ctypes
from ctypes import *
from datetime import datetime
import math
import os
import numpy
import random

import statistics


def func(x):
    sum = 0
    for t in x:
        sum = sum + t
    return sum / len(x)


def test_cpp(x):
    os.system("g++ -fPIC -shared -o func.so func.cpp")
    path = os.path.join(os.getcwd(), 'func.so')
    cpp = CDLL(path)
    cpp.func_cpp.restype = c_double
    cpp.func_cpp.argtypes = [POINTER(c_double * len(x)), c_size_t]
    x = (c_double * len(x))(*x)
    start_time = datetime.now()

    # cast(x, POINTER(c_double))
    resultcpp = cpp.func_cpp(byref(x), len(x))
    print('CPP DLL TIME :  ')
    print("Result = ", resultcpp)
    print(datetime.now() - start_time)


def run_py(x):
    start_time = datetime.now()
    result = func(x)
    print('PYTHON TIME :  ')
    print("Result = ", result)
    print(datetime.now() - start_time)
    print('\n')


if __name__ == "__main__":
    x = numpy.array([(random.random() + random.random()) for i in range(199999990)])
    x = x.tolist()
    print('Начало теста \n')

    run_py(x)
    test_cpp(x)

    # print(f"In Python: int: {x}  return {result}")

## cpp - 2.45
## python 3.8


# cpp 0:00:00.038000
## python 0:00:00.019000


from ctypes import *

import numpy as np
import random
import time

import os


def func_native_python(array: list) -> float:
    res = 0
    for x in array:
        res += x
    return res/len(array)


if __name__ == "__main__":

    ## Create test Array

    array = [random.random() for i in range(1000000)]

    ## Native Python

    print('\n')
    t0 = time.time()
    result_netive_py = func_native_python(array)
    t1 = time.time()
    print(f"Native Python Func\nTime = {(t1 - t0) * 1000} ms \nResult = {result_netive_py}")

    ##  Numpy
    print('\n')
    array_np = np.array(array)
    t0 = time.time()
    result_numpy = np.mean(array_np)
    t1 = time.time()
    print(f"Numpy Func\nTime = {(t1 - t0) * 1000} ms \nResult = {result_numpy}")

    ## C++ dll import

    print('\n')
    path = os.path.join(os.getcwd(), 'lib.so')
    cpp = CDLL(path, winmode=1)
    # cpp.func_cpp.argtypes = [POINTER(c_float * len(array)), c_ulonglong]

    array_x = (c_float * len(array))(*array)

    # print(array_x, hex(id(array_x)), byref(array_x), pointer(array_x))

    t0 = time.time()
    result_cpp_import = cpp.func_cpp(array_x, len(array))
    t1 = time.time()
    print(f"CPP import Func\nTime = {(t1 - t0) * 1000} ms \nResult = {result_cpp_import}")

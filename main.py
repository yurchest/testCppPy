import math
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

    t0 = time.time()
    array_np = np.array(array)
    result_numpy = np.mean(array_np)
    t1 = time.time()
    print(f"Numpy Func\nTime = {(t1 - t0) * 1000} ms \nResult = {result_numpy}")

    ## C++ dll import

    print("\n")
    os.system("g++ -fPIC -shared -o lib.so func.cpp")
    path = os.path.join(os.getcwd(), 'lib.so')
    cpp = CDLL(path)
    cpp.func_cpp.restype = c_float
    cpp.func_cpp.argtypes = [POINTER(c_float * len(array)), c_ulonglong]

    array_x = (c_float * len(array))(*array)
    leng = c_ulonglong(len(array))

    print(f"{hex(id(array_x))} --- {byref(array_x)} --- {byref(array_x)}")

    t0 = time.time()
    result_cpp_import = cpp.func_cpp(byref(array_x), leng)
    t1 = time.time()
    print(f"CPP import Func\nTime = {(t1 - t0) * 1000} ms \nResult = {result_cpp_import}")


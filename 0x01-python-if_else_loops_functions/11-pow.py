#!/usr/bin/python3
def pow(a, b):
    res = a
    for i in range(b):
        res *= a
    return res

#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            up = ord(i) - 32
        else:
            up = ord(i)
        print("{:c}".format(up), end="")
    print("")

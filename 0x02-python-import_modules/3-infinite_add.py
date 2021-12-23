#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    len = len(argv)

    sum = 0

    for i in range(1, len):
        num = int(argv[i])
        sum += num
    print("{}".format(sum))

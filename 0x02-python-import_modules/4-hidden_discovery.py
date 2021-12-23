#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    values = dir()

    for i in range(len(values)):
        if not values[i][0:2] == "__":
            print("{}".format(values[i]))

#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print("{:d}".format((-1 * number) % 10))
        return ((-1 * number) % 10)
    else:
        print("{:d}".format(number % 10))
        return (number % 10)

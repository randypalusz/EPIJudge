from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    if x == 0:
        return '0'
    isNegative = False
    reversedOutString = ""
    if x < 0:
        x = -x
        isNegative = True
    while x > 0:
        reversedOutString += chr(ord('0') + (x % 10))
        x = int(x/10)
    if isNegative:
        return '-' + reversedOutString[::-1]
    else:
        return reversedOutString[::-1]


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    isNegative = False
    out = 0
    multiplier = 1
    if s[0] is '-':
        isNegative = True
        s = s[1:]
    elif s[0] is '+':
        s = s[1:]
    for c in s[::-1]:
        out += int(c) * multiplier
        multiplier *= 10
    if isNegative:
        return -out
    return out


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))

from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    numOddBits = 0
    while x:
        isOdd = x & 1
        numOddBits += isOdd
        x = x >> 1
    return int(numOddBits % 2 != 0)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))

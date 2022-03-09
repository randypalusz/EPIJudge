from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    vals = []
    for i in range(n+1):
        if i == 0:
            vals.append(0)
        elif i == 1:
            vals.append(1)
        else:
            vals.append(vals[i-1] + vals[i-2])
    return vals[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))

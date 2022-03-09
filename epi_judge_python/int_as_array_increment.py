from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    A[-1] += 1
    for idx, _ in reversed(list(enumerate(A))):
        if idx == 0:
            continue
        if A[idx] >= 10:
            A[idx] -= 10
            A[idx-1] += 1

    if A[0] >= 10:
        A[0] -= 10
        A.insert(0, 1)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))

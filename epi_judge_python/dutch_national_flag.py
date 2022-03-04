import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # cache the value to pivot against
    pivotValue = A[pivot_index]
    # markers (indices) for the groupings
    lower, equal, higher = 0, 0, len(A)
    # up to this point, 0 -> 0 are known, and all the unknown elements lie within
    # 0 (equal) and len(A) (higher), so until these two numbers are equal, we have
    # un-traversed elements
    while equal < higher:
        if A[equal] < pivotValue:
            A[equal], A[lower] = A[lower], A[equal]
            equal += 1
            lower += 1
        elif A[equal] == pivotValue:
            equal += 1
        else:  # if A[equal] > pivotValue
            higher -= 1
            A[equal], A[higher] = A[higher], A[equal]
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

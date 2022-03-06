import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    out = []
    min_heap = []
    iters = [iter(x) for x in sorted_arrays]
    for idx, iterator in enumerate(iters):
        element = next(iterator, None)
        if element is not None:
            heapq.heappush(min_heap, (element, idx))

    while min_heap:
        element, iterator_index = heapq.heappop(min_heap)
        out.append(element)
        current_iterator = iters[iterator_index]
        next_element = next(current_iterator, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, iterator_index))
    return out


def bf_merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    ret = []
    # array keeping track of the given indices
    min_heap = [0] * len(sorted_arrays)
    for idx, val in enumerate(sorted_arrays):
        min_heap[idx] = val.pop(0)
    while not all(element == float("inf") for element in min_heap):
        # get min value in min_heap
        min_val = min(min_heap)
        idx = min_heap.index(min_val)
        ret.append(min_heap[idx])
        if sorted_arrays[idx]:
            min_heap[idx] = sorted_arrays[idx].pop(0)
        else:
            min_heap[idx] = float("inf")

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))

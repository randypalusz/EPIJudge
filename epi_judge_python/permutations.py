from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    def helper(in_list: List[int], current_perm: List[int], all_perms: List[List[int]]):
        if not in_list:
            all_perms.append(current_perm)
            return
        for idx, val in enumerate(in_list):
            helper(in_list[:idx] + in_list[idx+1:],
                   current_perm + [val], all_perms)
    all_permutations = []
    helper(A, [], all_permutations)

    return all_permutations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

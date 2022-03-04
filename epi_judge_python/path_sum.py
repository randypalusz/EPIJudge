from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    # TODO - you fill in here.
    def sum_helper(node: BinaryTreeNode, remaining_weight: int):
        if not node:
            return False
        remaining_weight -= node.data
        # if at a leaf - return the status of remaining_weight
        if not node.left and not node.right:
            return remaining_weight == 0
        return sum_helper(node.left, remaining_weight) or sum_helper(node.right, remaining_weight)

    return sum_helper(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))

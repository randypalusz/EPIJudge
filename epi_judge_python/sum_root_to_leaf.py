from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_helper(node: BinaryTreeNode, sum_to_this_point):
        if not node:
            # we're at the end
            return 0
        # within tree
        sum_to_this_point = (sum_to_this_point << 1) + node.data
        if not node.left and not node.right:
            return sum_to_this_point
        l_result = sum_helper(node.left, sum_to_this_point)
        r_result = sum_helper(node.right, sum_to_this_point)
        return l_result + r_result

    return sum_helper(tree,  0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))

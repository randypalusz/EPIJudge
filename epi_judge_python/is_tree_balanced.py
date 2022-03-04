from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# mine


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def check_balanced(tree: BinaryTreeNode):
        # return structure (balanced: bool, height: int)
        if not tree:
            return (True, 0)
        l_result = check_balanced(tree.left)
        if not l_result[0]:
            return l_result
        r_result = check_balanced(tree.right)
        if not r_result[0]:
            return r_result

        balanced = abs(l_result[1] - r_result[1]) <= 1
        height = max(l_result[1], r_result[1]) + 1
        return (balanced, height)

    return check_balanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

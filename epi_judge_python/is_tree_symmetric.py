from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def check_symmetry(l_tree: BinaryTreeNode, r_tree: BinaryTreeNode) -> bool:
        if not l_tree and not r_tree:
            return True
        if (l_tree and not r_tree) or (not l_tree and r_tree):  # if only one or the other exists
            return False

        elements_equal = l_tree.data == r_tree.data
        return check_symmetry(l_tree.left, r_tree.right) and check_symmetry(l_tree.right, r_tree.left) and elements_equal

    if not tree:
        return True
    else:
        return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))

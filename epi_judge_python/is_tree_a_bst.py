from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def traverse(tree: BinaryTreeNode, low=float('-inf'), high=float('inf')):
        if not tree:
            return True
        elif not low <= tree.data <= high:
            return False
        return traverse(tree.left, low, tree.data) and traverse(tree.right, tree.data, high)
    return traverse(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))

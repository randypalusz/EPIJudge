import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    # will return tuple: (int, BinaryTreeNode) -> (count of node0 + node1 in subtree, ancestor)
    def lca_recursion(current_tree: BinaryTreeNode):
        if not current_tree:
            return (0, None)
        l_result = lca_recursion(current_tree.left)
        # need these == 2 checks:
        #   if not checking for this, then when going up the stack, we will keep seeing that
        #   the num_target_nodes == 2, and the ancestor will keep getting updated, thus
        #   returning not the LCA, but the root every time
        if l_result[0] == 2:
            return l_result
        r_result = lca_recursion(current_tree.right)
        if r_result[0] == 2:
            return r_result
        num_target_nodes = (
            l_result[0] + r_result[0] + (node0, node1).count(current_tree))
        return (num_target_nodes, current_tree if num_target_nodes == 2 else None)

    return lca_recursion(tree)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

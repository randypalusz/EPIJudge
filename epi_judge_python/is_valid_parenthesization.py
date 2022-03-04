from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    lookup = {'(': ')', '{': '}', '[': ']'}
    left_side_stack = []
    for char in s:
        if char in lookup:
            left_side_stack.append(char)
        elif char not in lookup.values():
            continue
        elif char in lookup.values() and not left_side_stack:
            return False
        elif char in lookup.values() and lookup[left_side_stack.pop()] != char:
            return False

    return not left_side_stack


def ais_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    closedToOpenMap = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        # if a valid left-side parentheses character
        if char in closedToOpenMap:
            stack.append(char)
        # if a right-side parentheses
        elif not stack or closedToOpenMap[stack.pop()] != char:
            return False
        # if not a parentheses character, don't do anything
        else:
            continue

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))

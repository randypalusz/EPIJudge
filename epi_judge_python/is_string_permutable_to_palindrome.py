from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    hist = {}
    # iterate over string
    # add into map when char first seen
    # otherwise if already seen, increment num by 1
    for char in s:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] = hist[char] + 1
    # get list of whether each char is seen an odd number of times
    num_odd = [val % 2 != 0 for val in hist.values()]
    # return True if the odd count <= 1
    return num_odd.count(True) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))

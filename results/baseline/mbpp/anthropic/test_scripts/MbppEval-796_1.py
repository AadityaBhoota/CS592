def return_sum(d):
    """
    Write a function to find the sum of all items in the given dictionary.

    Examples:
    return_sum({'a': 100, 'b':200, 'c':300}) == 600
    return_sum({'a': 25, 'b':18, 'c':45}) == 88
    return_sum({'a': 36, 'b':39, 'c':49}) == 124
    """
    return sum(d.values())

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124

check(return_sum)
def total_match(lst1, lst2):
    def calculate_chars(lst):
        return sum(len(s) for s in lst)

    if len(lst1) == len(lst2):
        total_chars_lst1 = calculate_chars(lst1)
        total_chars_lst2 = calculate_chars(lst2)

        if total_chars_lst1 < total_chars_lst2:
            return lst1
        else:
            return lst2
    elif len(lst1) < len(lst2):
        return lst1
    else:
        return lst2

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']


    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([], ['this']) == []
    assert candidate(['this'], []) == []


check(total_match)
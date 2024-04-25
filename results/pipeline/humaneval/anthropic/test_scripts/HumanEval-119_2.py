def is_balanced(s):
    open_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        else:
            if open_count == 0:
                return False
            open_count -= 1
    return open_count == 0

def match_parens(lst):
    s1, s2 = lst
    if is_balanced(s1 + s2) or is_balanced(s2 + s1):
        return 'Yes'
    else:
        return 'No'

def check(candidate):

    # Check some simple cases
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    

    # Check some edge cases that are easy to work out by hand.
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes' 


check(match_parens)
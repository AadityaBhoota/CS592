def match_parens(lst):
    open_count = 0
    for s in lst:
        for char in s:
            if char == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                return 'No'
    if open_count == 0:
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
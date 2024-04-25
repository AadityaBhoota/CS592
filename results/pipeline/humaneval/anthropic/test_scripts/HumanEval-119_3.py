def match_parens(lst):
    if len(lst) != 2:
        return 'No'

    can_be_matched = False

    for string in lst:
        open_count = 0
        close_count = 0
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
        if open_count == close_count:
            can_be_matched = True
            break

    if can_be_matched:
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
def match_parens(lst):
    count = 0

    for s in lst:
        for c in s:
            if c == '(':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    return 'No'

    if count == 0:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'

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
def match_parens(lst):
    s1, s2 = lst
    stack = []
    
    # Check if the first string is valid
    for c in s1:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'No'
            stack.pop()
    
    # Check if the second string is valid
    for c in s2:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'Yes'
            stack.pop()
    
    # If the stack is empty, it means both strings are valid
    return 'Yes' if not stack else 'No'

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
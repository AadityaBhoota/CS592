def match_parens(lst):
    def is_balanced(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    open_count = 0
    close_count = 0

    for string in lst:
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1

    if open_count == close_count:
        return 'Yes'
    elif open_count > 0 and close_count > 0:
        return 'Yes'
    else:
        return 'No'

# Test cases



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
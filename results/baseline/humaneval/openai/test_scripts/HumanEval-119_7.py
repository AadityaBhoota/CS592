def match_parens(lst):
    # Concatenate the two strings
    concatenated_string = lst[0] + lst[1]

    # Check if the concatenated string contains balanced parentheses
    stack = []
    for char in concatenated_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return 'No'

    # Return 'Yes' if stack is empty (all parentheses are balanced)
    return 'Yes' if not stack else 'No'

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
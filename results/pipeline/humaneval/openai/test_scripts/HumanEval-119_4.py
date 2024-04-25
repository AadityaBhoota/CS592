def match_parens(lst):
    open_count = lst[0].count('(') + lst[1].count('(')
    close_count = lst[0].count(')') + lst[1].count(')')
    
    balance_diff = open_count - close_count
    
    if balance_diff % 2 == 0:
        for i in range(len(lst)):
            if balance_diff == 0:
                break
            for j in range(len(lst[i])):
                if lst[i][j] == '(':
                    balance_diff -= 1
                    lst[i] = lst[i][:j] + lst[i][j+1:]
                    break
        
        if balance_diff == 0:
            for s in lst:
                for c in s:
                    if c == ')':
                        return 'No'
            return 'Yes'
    
    return 'No'

# Test the function with examples



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
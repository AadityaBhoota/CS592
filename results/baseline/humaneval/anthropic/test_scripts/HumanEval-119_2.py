def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    
    # Count the number of open and close parentheses in each string
    open_count1, close_count1 = 0, 0
    open_count2, close_count2 = 0, 0
    
    for char in lst[0]:
        if char == '(':
            open_count1 += 1
        else:
            close_count1 += 1
    
    for char in lst[1]:
        if char == '(':
            open_count2 += 1
        else:
            close_count2 += 1
    
    # Check if the total number of open and close parentheses are equal
    if (open_count1 + open_count2) == (close_count1 + close_count2):
        # Check if the strings can be concatenated in some order to make a good string
        if (open_count1 >= close_count2 and close_count1 >= open_count2) or \
           (open_count2 >= close_count1 and close_count2 >= open_count1):
            return 'Yes'
    
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
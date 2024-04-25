import re
def start_withp(words):
    '''
    Write a function to return two words from a list of words starting with letter 'p'.

    Examples:
    start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
    start_withp(["Python Programming","Java Programming"]) == ('Python','Programming')
    start_withp(["Pqrst Pqr","qrstuv"]) == ('Pqrst','Pqr')
    '''
    # Initialize an empty list to store words starting with 'p'
    result = []
    
    # Iterate through each word in the input list
    for word in words:
        # Use regular expression to find words starting with letter 'p'
        match = re.findall(r'\bP\w+', word)
        if match:
            result.extend(match)
    
    # Return first two words starting with 'p'
    return tuple(result[:2])

# Test the function with examples




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
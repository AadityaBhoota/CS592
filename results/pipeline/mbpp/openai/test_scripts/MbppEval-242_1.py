def count_charac(str1):
    '''
    Write a function to count the total number of characters in a string.

    Examples:
    count_charac("python programming") == 18
    count_charac("language") == 8
    count_charac("words") == 5
    '''
    count = 0
    
    for char in str1:
        count += 1
    
    return count

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)
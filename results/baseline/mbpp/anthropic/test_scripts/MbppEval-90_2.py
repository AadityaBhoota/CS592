def len_log(list1):
    '''
    Write a python function to find the length of the longest word.

    Examples:
    len_log(["python","PHP","bigdata"]) == 7
    len_log(["a","ab","abc"]) == 3
    len_log(["small","big","tall"]) == 5
    '''
    # Initialize the maximum length to 0
    max_len = 0
    
    # Iterate through the list of words
    for word in list1:
        # Check if the length of the current word is greater than the current maximum
        if len(word) > max_len:
            # If so, update the maximum length
            max_len = len(word)
    
    # Return the maximum length
    return max_len

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5

check(len_log)
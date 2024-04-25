def count_occurance(s):
    '''
    Write a function to count the number of occurence of the string 'std' in a given string.

    Examples:
    count_occurance("letstdlenstdporstd") == 3
    count_occurance("truststdsolensporsd") == 1
    count_occurance("makestdsostdworthit") == 2
    '''
def count_occurrence(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'std':
            count += 1
    return count

def check(candidate):
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2
    assert count_occurance("stds") == 1
    assert count_occurance("") == 0

check(count_occurance)
def number_of_substrings(string): 
    count = 0
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            count += 1
    
    return count

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)
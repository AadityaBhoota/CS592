def anti_shuffle(s):
    words = s.split(' ')
    
    # Sort the characters in each word based on ASCII values
    sorted_words = [''.join(sorted(word, key=lambda x: ord(x))) for word in words]
    
    # Join the modified words back together along with the blank spaces
    ordered_string = ' '.join(sorted_words)
    
    return ordered_string

def check(candidate):

    # Check some simple cases
    assert candidate('Hi') == 'Hi'
    assert candidate('hello') == 'ehllo'
    assert candidate('number') == 'bemnru'
    assert candidate('abcd') == 'abcd'
    assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
    assert candidate('') == ''
    assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
    # Check some edge cases that are easy to work out by hand.
    assert True


check(anti_shuffle)
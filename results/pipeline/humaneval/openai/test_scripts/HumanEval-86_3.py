import re

def sort_word(word):
    return ''.join(sorted(word, key=lambda c: ord(c)))

def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of a string is a string where all words are replaced by a new word 
    with characters arranged in ascending order of ascii value.
    
    Args:
    - s: input string
    
    Returns:
    - Ordered version of the input string
    """
    words = re.findall(r'\S+|\s+', s)
    ordered_words = [sort_word(word) if word.strip() else ' ' for word in words]
    ordered_string = ''.join(ordered_words)
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
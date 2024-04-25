def anti_shuffle(s):
    words = s.split()
    sorted_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_words.append(sorted_word)
    result = ' '.join(sorted_words)
    return result

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
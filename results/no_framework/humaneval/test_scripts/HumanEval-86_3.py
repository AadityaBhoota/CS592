def anti_shuffle(s):
    def order_word(word):
        return ''.join(sorted(word))

    words = s.split()
    ordered_words = [order_word(word) for word in words]

    ordered_sentence = ' '.join(ordered_words)
    return ordered_sentence

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'

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
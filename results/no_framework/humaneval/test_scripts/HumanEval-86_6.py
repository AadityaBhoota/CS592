def anti_shuffle(s):
    def sort_word(word):
        # Sort the characters in the word based on ascii value
        sorted_word = ''.join(sorted(word))
        return sorted_word
    
    # Split the original string into words
    words = s.split(' ')
    
    # Apply sort_word function to each word and join them back with space
    sorted_words = [sort_word(word) for word in words]
    sorted_sentence = ' '.join(sorted_words)
    
    return sorted_sentence

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
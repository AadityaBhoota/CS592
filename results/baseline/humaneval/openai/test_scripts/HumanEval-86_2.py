def anti_shuffle(s):
    def sort_word(word):
        return ''.join(sorted(word))

    result = []
    current_word = ''
    
    for char in s:
        if char.isalpha():
            current_word += char
        else:
            if current_word:
                result.append(sort_word(current_word))
                current_word = ''
            result.append(char)

    if current_word:
        result.append(sort_word(current_word))
    
    return ''.join(result)

# Test cases




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
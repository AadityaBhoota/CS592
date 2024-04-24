def anti_shuffle(s):
    def order_word(word):
        return ''.join(sorted(word))

    result = []
    start = 0
    for i, char in enumerate(s):
        if char.isspace() or i == len(s) - 1:
            if i == len(s) - 1:
                word = s[start:i + 1].strip()
            else:
                word = s[start:i].strip()
            result.append(order_word(word) + char)
            start = i + 1

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
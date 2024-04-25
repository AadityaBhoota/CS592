import math

def prime_length(string):
    if len(string) < 2:
        return False

    for i in range(2, int(math.sqrt(len(string)))+1):
        if len(string) % i == 0:
            return False
    return True

def check(candidate):

    # Check some simple cases
    assert candidate('Hello') == True
    assert candidate('abcdcba') == True
    assert candidate('kittens') == True
    assert candidate('orange') == False
    assert candidate('wow') == True
    assert candidate('world') == True
    assert candidate('MadaM') == True
    assert candidate('Wow') == True
    assert candidate('') == False
    assert candidate('HI') == True
    assert candidate('go') == True
    assert candidate('gogo') == False
    assert candidate('aaaaaaaaaaaaaaa') == False

    # Check some edge cases that are easy to work out by hand.
    assert candidate('Madam') == True
    assert candidate('M') == False
    assert candidate('0') == False


check(prime_length)
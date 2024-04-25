def is_consonant(char):
    """
    Helper function to check if a character is a consonant.
    """
    return char.isalpha() and char.lower() not in 'aeiou'

def select_words(s, n):
    """
    Given a string s and a natural number n, returns a list of all words from string s
    that contain exactly n consonants, in the order they appear in the string s.
    If the string s is empty, the function returns an empty list.
    """
    if not s:
        return []

    words = s.split()
    result = []

    for word in words:
        consonant_count = sum(1 for char in word if is_consonant(char))
        if consonant_count == n:
            result.append(word)

    return result

def check(candidate):

    # Check some simple cases
    assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))      
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))  
    assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))      
    assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))  
    assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))


    # Check some edge cases that are easy to work out by hand.
    assert candidate("", 4) == [], "1st edge test error: " + str(candidate("", 4))
    assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"], "2nd edge test error: " + str(candidate("a b c d e f", 1))


check(select_words)
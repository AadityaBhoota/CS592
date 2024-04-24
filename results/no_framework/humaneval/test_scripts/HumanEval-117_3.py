def is_consonant(char):
    return char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']

def count_consonants(word):
    return sum(is_consonant(char) for char in word)

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result

# Test cases
print(select_words("Mary had a little lamb", 4))  # ==> ["little"]
print(select_words("Mary had a little lamb", 3))  # ==> ["Mary", "lamb"]
print(select_words("simple white space", 2))  # ==> []
print(select_words("Hello world", 4))  # ==> ["world"]
print(select_words("Uncle sam", 3))  # ==> ["Uncle"]

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
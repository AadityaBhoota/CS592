def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ','. If no commas exist, return the number of lowercase letters with odd order in the
    alphabet, where ord('a') = 0, ord('b') = 1, ... ord('z') = 25.

    Examples:
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    # Split the text on whitespace
    words = txt.split()
    
    # If no whitespace exists, split on commas
    if not words:
        words = txt.split(',')
    
    # If no commas exist, return the number of lowercase letters with odd order in the alphabet
    if not words:
        odd_order_count = 0
        for char in txt.lower():
            if char.isalpha() and (ord(char) - ord('a')) % 2 == 0:
                odd_order_count += 1
        return odd_order_count
    
    return words

def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3
    assert candidate("aaabb") == 2
    assert candidate("aaaBb") == 1
    assert candidate("") == 0

check(split_words)
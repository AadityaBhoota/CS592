def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace.
    If the input string contains no whitespace and no commas, return the count of lowercase letters with odd order in the alphabet.
    Examples:
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    '''
    words = txt.split()
    if len(words) == 1 and ',' not in words[0]:
        return sum(1 for c in words[0].lower() if ord(c) % 2 == 1)
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
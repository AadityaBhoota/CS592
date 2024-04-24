def split_words(txt):
    import string
    
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        txt = txt.replace(',', ' ')
        words = txt.split()
        if len(words) > 1:
            return words
        else:
            count = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
            return count

# Test cases




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
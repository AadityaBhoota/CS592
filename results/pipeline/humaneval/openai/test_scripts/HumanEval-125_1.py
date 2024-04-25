def split_words(txt):
    if ' ' in txt:
        return txt.split()
    
    if ',' in txt:
        return txt.split(',')

    count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
    return count

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
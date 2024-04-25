def split_words(txt):
    words = txt.split(',')
    if len(words) > 1:
        return words

    words = txt.split()
    if len(words) > 1:
        return words

    odd_count = 0
    for char in txt:
        if char.islower():
            ord_value = ord(char) - ord('a')
            if ord_value % 2 == 1:
                odd_count += 1
    return odd_count

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
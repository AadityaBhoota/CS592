def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return [char for char in txt if char.islower() and ord(char) % 2 == 1]

# Test cases
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))  # ➞ 3

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
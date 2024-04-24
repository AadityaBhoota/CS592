def split_words(txt):
    words = txt.split()
    if len(words) == 1 and ',' in txt:
        words = txt.split(',')
    if len(words) == 1:
        count = sum(1 for char in txt if char.islower() and ord('a') % 2 != 0)
        return count
    return words

# Examples
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
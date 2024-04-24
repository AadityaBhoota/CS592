def split_words(txt):
    # Check if the text contains any whitespaces
    if ' ' in txt:
        return txt.split()
    # Check if the text contains any commas
    elif ',' in txt:
        return txt.split(',')
    # Count the number of lower-case letters with odd order in the alphabet
    odd_alphabets = [char for char in txt if char.islower() and ord(char) % 2 != 0]
    return len(odd_alphabets)

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
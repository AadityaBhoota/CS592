def split_words(txt):
    # Check if the text contains whitespace
    if ' ' in txt:
        # Split the text on whitespaces
        return txt.split()
    # Check if the text contains commas
    elif ',' in txt:
        # Split the text on commas
        return txt.split(',')
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count

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
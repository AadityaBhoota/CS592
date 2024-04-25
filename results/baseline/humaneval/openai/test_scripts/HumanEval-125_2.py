def split_words(txt):
    # Check if there are any white spaces in the text
    if ' ' in txt:
        return txt.split()  # Split the words based on white spaces
    # Check if there are any commas in the text
    elif ',' in txt:
        return txt.split(',')  # Split the words based on commas
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        count = sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
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
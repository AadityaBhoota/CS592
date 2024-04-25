def split_words(txt):
    is_whitespace_present = ' ' in txt
    
    if is_whitespace_present:
        return txt.split()
    else:
        is_comma_present = ',' in txt
        
        if is_comma_present:
            return txt.split(',')
        else:
            count_odd_lowercase = sum(1 for char in txt if 'a' <= char <= 'z' and ord(char) % 2 != 0)
            return count_odd_lowercase

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
def split_words(txt):
    has_whitespace = ' ' in txt
    
    if has_whitespace:
        words = txt.split()
        return words
    
    has_commas = ',' in txt
    
    if not has_whitespace and has_commas:
        words = txt.split(',')
        return [word.strip() for word in words]
    
    if not has_whitespace and not has_commas:
        count_odd_lower_case_letters = 0
        txt_lower = txt.lower()
        
        for char in txt_lower:
            if char.islower() and ord(char) % 2 != 0:
                count_odd_lower_case_letters += 1
        
        return count_odd_lower_case_letters

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
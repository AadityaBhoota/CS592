import re

def start_withp(words):
    words_with_p = []
    for word in words:
        matches = re.findall(r'\bP\w+', word)
        words_with_p.extend(matches)
    
    if len(words_with_p) >= 2:
        return tuple(words_with_p[:2])
    elif len(words_with_p) == 1:
        return words_with_p[0], words_with_p[0]
    else:
        return None, None

# Test cases




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
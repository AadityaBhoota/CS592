import re

def start_withp(words):
    result = []
    pattern = re.compile(r'\bP\w+')
    for w in words:
        matches = pattern.findall(w)
        if len(matches) == 2:
            result.extend(matches)
    return tuple(result)

# Test cases




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
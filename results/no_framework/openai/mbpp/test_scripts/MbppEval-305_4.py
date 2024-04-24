import re

def start_withp(words):
    result = []
    for word in words:
        match = re.findall(r'\bP\w+', word)
        if len(match) >= 2:
            result.extend(match[:2])
    return tuple(result)

# Test the function with examples




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
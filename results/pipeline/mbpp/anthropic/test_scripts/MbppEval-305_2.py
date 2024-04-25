import re

def start_withp(words):
    result = []
    for word in words:
        if re.match(r'^p', word, re.IGNORECASE):
            result.append(word)
            if len(result) == 2:
                break
    return tuple(result)

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
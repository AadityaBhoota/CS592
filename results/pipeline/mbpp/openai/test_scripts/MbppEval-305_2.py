import re

def start_withp(words):
    p_words = []
    for word in words:
        p_words.extend(re.findall(r'\b[pP]\w+', word))
        
    return tuple(p_words[:2]) if len(p_words) >= 2 else None

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
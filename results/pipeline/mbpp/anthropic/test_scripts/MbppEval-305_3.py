import re

def start_withp(words):
    p_words = []
    P_words = []
    
    for word in words:
        if re.match(r'^p', word, re.IGNORECASE):
            if word.startswith('p'):
                p_words.append(word)
            else:
                P_words.append(word)
    
    return (p_words[0], P_words[0]) if p_words and P_words else ()

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
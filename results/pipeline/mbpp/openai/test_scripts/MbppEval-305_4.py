import re

def start_withp(words):
    p_words = []

    for word in words:
        split_words = word.split()

        for w in split_words:
            if w.lower().startswith('p'):
                p_words.append(w)

    return tuple(p_words[:2])

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
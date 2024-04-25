import re
def start_withp(words):
    p_words = []
    
    for word in words:
        word_list = word.split()
        for w in word_list:
            if re.match('p', w, re.I):
                p_words.append(w)
    
    return tuple(p_words[:2])

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
def start_withp(words):
    p_words = []
    for sentence in words:
        for word in sentence.split():
            if word.startswith('P') or word.startswith('p'):
                p_words.append(word)
    return tuple(p_words[:2])

# Test cases




def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
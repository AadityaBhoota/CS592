def start_withp(words):
    words_with_p = []
    for word in words:
        words_with_p += re.findall(r'\bP\w+', word)
    if len(words_with_p) >= 2:
        return tuple(words_with_p[:2])
    elif len(words_with_p) == 1:
        return words_with_p[0], ''
    else:
        return '', ''

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
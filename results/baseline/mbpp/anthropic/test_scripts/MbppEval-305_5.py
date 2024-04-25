import re

def start_withp(words):
    """
    Write a function to return two words from a list of words starting with letter 'p'.

    Examples:
    start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
    start_withp(["Python Programming","Java Programming"]) == ('Python','Programming')
    start_withp(["Pqrst Pqr","qrstuv"]) == ('Pqrst','Pqr')
    """
    p_words = []
    for word in words:
        if re.match(r'^p', word, re.IGNORECASE):
            p_words.append(word)
    if len(p_words) >= 2:
        return (p_words[0], p_words[1])
    elif len(p_words) == 1:
        return (p_words[0], '')
    else:
        return ('', '')

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
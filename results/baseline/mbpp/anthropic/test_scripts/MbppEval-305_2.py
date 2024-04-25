import re

def start_withp(words):
    """
    Write a function to return two words from a list of words starting with letter 'p'.

    Examples:
    start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
    start_withp(["Python Programming","Java Programming"]) == ('Python','Programming')
    start_withp(["Pqrst Pqr","qrstuv"]) == ('Pqrst','Pqr')
    """
    words_with_p = []
    for word in words:
        if word.lower().startswith("p"):
            words_with_p.append(word)
    
    if len(words_with_p) >= 2:
        return (words_with_p[0], words_with_p[1])
    elif len(words_with_p) == 1:
        return (words_with_p[0], words_with_p[0])
    else:
        return ("", "")

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
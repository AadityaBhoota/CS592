import re

def start_withp(words):
    """
    Write a function to return two words from a list of words starting with letter 'p'.

    Examples:
    start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
    start_withp(["Python Programming","Java Programming"]) == ('Python','Programming')
    start_withp(["Pqrst Pqr","qrstuv"]) == ('Pqrst','Pqr')
    """
    words_list = words
    p_words = []
    for word_pair in words_list:
        word_pair_list = word_pair.split()
        for word in word_pair_list:
            if word.startswith('p') or word.startswith('P'):
                p_words.append(word)
    if len(p_words) >= 2:
        return (p_words[0], p_words[1])
    else:
        return ()

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)
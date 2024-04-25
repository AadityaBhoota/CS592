def word_len(s):
    length = len(s)
    is_odd = length % 2 != 0
    return is_odd

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
def word_len(s):
    word_length = len(s)
    return word_length % 2 == 1

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
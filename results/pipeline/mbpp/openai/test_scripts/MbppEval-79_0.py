def word_len(s):
    word_length = len(s)
    is_odd_length = word_length % 2 != 0
    return is_odd_length

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
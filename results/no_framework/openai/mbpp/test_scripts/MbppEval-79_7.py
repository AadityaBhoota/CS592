def word_len(s):
    return len(s) % 2 == 1

# Test cases




def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
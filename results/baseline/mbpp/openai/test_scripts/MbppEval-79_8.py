def word_len(s):
    if len(s) % 2 == 0:
        return False
    else:
        return True

# Test cases




def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
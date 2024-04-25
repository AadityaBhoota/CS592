def word_len(s):
    word_length = len(s)
    
    if word_length % 2 == 0:
        return False
    else:
        return True

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)
def len_log(list1):
    max_length = 0
    
    for word in list1:
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5

check(len_log)
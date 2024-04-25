def len_log(list1):
    longest_length = 0
    for word in list1:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5

check(len_log)
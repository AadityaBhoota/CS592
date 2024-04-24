def len_log(list1):
    return max(len(word) for word in list1)

# Test the function with the examples provided




def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5

check(len_log)
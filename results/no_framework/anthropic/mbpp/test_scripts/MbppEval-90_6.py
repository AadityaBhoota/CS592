def len_log(list1):
    """
    Write a python function to find the length of the longest word.

    Examples:
    len_log(["python","PHP","bigdata"]) == 7
    len_log(["a","ab","abc"]) == 3
    len_log(["small","big","tall"]) == 5
    """
    if not list1:
        return 0
    return max(len(word) for word in list1)

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5

check(len_log)
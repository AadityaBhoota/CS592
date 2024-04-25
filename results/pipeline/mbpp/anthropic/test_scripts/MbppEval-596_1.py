import sys

def tuple_size(tuple_list):
    '''
    Write a function to find the size in bytes of the given tuple.

    Examples:
    tuple_size(("A", 1, "B", 2, "C", 3)) == 42
    tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu")) == 72
    tuple_size(((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))) == 80
    '''
    total_size = 0
    for tup in tuple_list:
        tup_size = 0
        for item in tup:
            tup_size += sys.getsizeof(item)
        total_size += tup_size
    return total_size

def check(candidate):
    assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    assert tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))

check(tuple_size)
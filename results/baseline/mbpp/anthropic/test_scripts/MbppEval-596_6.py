import sys

def tuple_size(tuple_list):
    '''
    Write a function to find the size in bytes of the given tuple.

    Examples:
    tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))
    '''
    return sys.getsizeof(tuple_list)

def check(candidate):
    assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    assert tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))

check(tuple_size)
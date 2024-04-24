def tup_string(tup1):
    """
    Write a function to convert a tuple to a string.

    Examples:
    tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
    tup_string(('p', 'y', 't', 'h', 'o', 'n')) == "python"
    tup_string(('p', 'r', 'o', 'g', 'r', 'a', 'm')) == "program"
    """
    return ''.join(tup1)

def check(candidate):
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert tup_string(('p','y','t','h','o','n'))==("python")
    assert tup_string(('p','r','o','g','r','a','m'))==("program")

check(tup_string)
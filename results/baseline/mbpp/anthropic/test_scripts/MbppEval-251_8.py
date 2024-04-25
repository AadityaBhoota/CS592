def insert_element(lst, element):
    """
    Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.

    Examples:
    insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
    insert_element(['python', 'java'], 'program') == ['program', 'python', 'program', 'java']
    insert_element(['happy', 'sad'], 'laugh') == ['laugh', 'happy', 'laugh', 'sad']
    """
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result

def check(candidate):
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']

check(insert_element)
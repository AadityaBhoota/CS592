def insert_element(lst, element):
    """
    Inserts the given element before each element in the input list.
    
    Args:
    lst (list): The input list.
    element (str): The element to be inserted.
    
    Returns:
    list: The resulting list with the element inserted before each element.
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
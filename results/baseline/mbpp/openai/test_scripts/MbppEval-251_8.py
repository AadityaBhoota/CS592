def insert_element(lst, element):
    new_lst = []
    for item in lst:
        new_lst.extend([element, item])
    return new_lst

# Test cases




def check(candidate):
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']

check(insert_element)
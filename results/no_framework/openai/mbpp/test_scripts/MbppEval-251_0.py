def insert_element(lst, element):
    new_lst = []
    for item in lst:
        new_lst.append(element)
        new_lst.append(item)
    return new_lst

# Testing the function with the examples provided



def check(candidate):
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']

check(insert_element)
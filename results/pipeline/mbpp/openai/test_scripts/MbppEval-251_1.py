def insert_element(lst, element):
    modified_list = []
    
    for item in lst:
        modified_list.append(element)
        modified_list.append(item)
        
    return modified_list

def check(candidate):
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']

check(insert_element)
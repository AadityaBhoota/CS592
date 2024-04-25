from operator import itemgetter

def index_minimum(test_list):
    min_value = float('inf')  # Initialize to a large value
    min_element = None
    
    for item in test_list:
        if item[1] < min_value:
            min_value = item[1]
            min_element = item[0]
    
    return min_element

def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
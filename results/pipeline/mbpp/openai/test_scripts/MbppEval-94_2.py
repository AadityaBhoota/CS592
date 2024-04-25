from operator import itemgetter

def index_minimum(test_list):
    min_second_value = float('inf')  # Initialize with positive infinity to find the smallest value
    min_first_value = None
    
    for first_value, second_value in test_list:
        if second_value < min_second_value:
            min_second_value = second_value
            min_first_value = first_value
    
    return min_first_value

def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
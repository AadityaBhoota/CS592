from operator import itemgetter 

def index_minimum(test_list):
    min_tuple = None
    min_second_val = float('inf')
    for item in test_list:
        name, value = item
        if value < min_second_val:
            min_second_val = value
            min_tuple = item

    return min_tuple[0]

# Test the function




def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
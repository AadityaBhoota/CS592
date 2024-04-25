from operator import itemgetter 

def index_minimum(test_list):
    min_value = float('inf')
    
    for name, value in test_list:
        if value < min_value:
            min_value = value

    result = next(filter(lambda x: x[1] == min_value, test_list))[0]

    return result

def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
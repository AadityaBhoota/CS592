from operator import itemgetter

def index_minimum(test_list):
    min_val = min(test_list, key=itemgetter(1))[1]
    for item in test_list:
        if item[1] == min_val:
            return item[0]

# Test cases




def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
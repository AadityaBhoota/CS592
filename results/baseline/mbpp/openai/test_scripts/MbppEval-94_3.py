from operator import itemgetter

def index_minimum(test_list):
    # Find the tuple with the smallest second value
    min_tuple = min(test_list, key=itemgetter(1))
    
    # Return the first value of the tuple with the smallest second value
    return min_tuple[0]

# Test cases




def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
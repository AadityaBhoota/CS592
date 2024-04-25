from operator import itemgetter

def index_minimum(test_list):
    # Get the index of the minimum value in the list of tuples based on the second element of each tuple
    min_index = min(enumerate(test_list), key=lambda x: x[1][1])[0]

    # Return the first element of the tuple at the minimum index
    return test_list[min_index][0]

# Test cases




def check(candidate):
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

check(index_minimum)
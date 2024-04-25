def extract_string(lst, size):
    result = []
    for s in lst:
        if len(s) == size:
            result.append(s)
    return result

# Testing the function with the given examples




def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)
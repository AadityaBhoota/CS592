def extract_string(str_list, length):
    return [word for word in str_list if len(word) == length]

# Test cases




def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)
def extract_string(str_list, length):
    extracted_strings = []

    for string in str_list:
        if len(string) >= length:
            extracted_strings.append(string)
    
    return extracted_strings

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)
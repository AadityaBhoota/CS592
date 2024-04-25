def extract_string(str, l):
    extracted_strings = []  
  
    for s in str: 
        if len(s) == l:  
            extracted_strings.append(s)  
    
    return extracted_strings  

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)
NO_OF_CHARS = 256

def str_to_list(string): 
    dirty_chars = [False] * NO_OF_CHARS
    
    for char in string: 
        dirty_chars[ord(char)] = True
        
    return dirty_chars

def remove_dirty_chars(str1, str2):
    dirty_chars_list = str_to_list(str2)
    
    filtered_str = ""
    
    for char in str1:
        if not dirty_chars_list[ord(char)]:
            filtered_str += char
    
    return filtered_str

def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)
NO_OF_CHARS = 256

def str_to_list(string): 
    # Creating a hash table to keep track of characters from string2
    hash_table = [0] * NO_OF_CHARS

    # Populating the hash_table with characters from string2
    for char in string2:
        hash_table[ord(char)] = 1

    # Filtering out characters from string1 which are not in string2
    result = ''.join([char for char in string1 if hash_table[ord(char)] == 0])
    
    return result

# Test cases




def check(candidate):
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

check(str_to_list)
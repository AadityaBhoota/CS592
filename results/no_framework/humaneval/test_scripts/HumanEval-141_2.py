def file_name_check(file_name):
    digits_count = sum(char.isdigit() for char in file_name)
    dot_count = file_name.count('.')
    if digits_count > 3 or dot_count != 1:
        return 'No'
    
    file_parts = file_name.split('.')
    if len(file_parts) != 2:
        return 'No'
    
    prefix, suffix = file_parts[0], file_parts[1]
    if not prefix or not prefix[0].isalpha():
        return 'No'

    valid_suffixes = ['txt', 'exe', 'dll']
    if suffix not in valid_suffixes:
        return 'No'
    
    return 'Yes'

# Test cases
print(file_name_check("example.txt"))     # => 'Yes'
print(file_name_check("1example.dll"))    # => 'No'
print(file_name_check("file_name.txt"))   # => 'No'
print(file_name_check("example"))         # => 'No'

def check(candidate):

    # Check some simple cases
    assert candidate("example.txt") == 'Yes'
    assert candidate("1example.dll") == 'No'
    assert candidate('s1sdf3.asd') == 'No'
    assert candidate('K.dll') == 'Yes'
    assert candidate('MY16FILE3.exe') == 'Yes'
    assert candidate('His12FILE94.exe') == 'No'
    assert candidate('_Y.txt') == 'No'
    assert candidate('?aREYA.exe') == 'No'
    assert candidate('/this_is_valid.dll') == 'No'
    assert candidate('this_is_valid.wow') == 'No'
    assert candidate('this_is_valid.txt') == 'Yes'
    assert candidate('this_is_valid.txtexe') == 'No'
    assert candidate('#this2_i4s_5valid.ten') == 'No'
    assert candidate('@this1_is6_valid.exe') == 'No'
    assert candidate('this_is_12valid.6exe4.txt') == 'No'
    assert candidate('all.exe.txt') == 'No'
    assert candidate('I563_No.exe') == 'Yes'
    assert candidate('Is3youfault.txt') == 'Yes'
    assert candidate('no_one#knows.dll') == 'Yes'
    assert candidate('1I563_Yes3.exe') == 'No'
    assert candidate('I563_Yes3.txtt') == 'No'
    assert candidate('final..txt') == 'No'
    assert candidate('final132') == 'No'
    assert candidate('_f4indsartal132.') == 'No'
    
        

    # Check some edge cases that are easy to work out by hand.
    assert candidate('.txt') == 'No'
    assert candidate('s.') == 'No'


check(file_name_check)
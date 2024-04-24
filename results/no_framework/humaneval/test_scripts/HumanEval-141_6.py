import re

def file_name_check(file_name):
    # Check if there are more than three digits in the file_name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    
    # Split the file name into two parts based on the dot
    parts = file_name.split('.')
    
    # Check if there is exactly one dot in the file name
    if len(parts) != 2:
        return 'No'
    
    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not parts[0][0].isalpha():
        return 'No'
    
    # Check if the substring after the dot is either 'txt', 'exe', or 'dll'
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# Test cases
print(file_name_check("example.txt"))      # => 'Yes'
print(file_name_check("1example.dll"))     # => 'No'
print(file_name_check("file_name.exe"))    # => 'Yes'
print(file_name_check("file_name.py"))     # => 'No'

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
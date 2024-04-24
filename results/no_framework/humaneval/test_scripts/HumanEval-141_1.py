def file_name_check(file_name):
    # Condition 1: Check for the number of digits in the file name
    if sum(char.isdigit() for char in file_name) > 3:
        return 'No'
    
    # Split the file name into two parts using the dot separator
    parts = file_name.split('.')
    
    # Condition 2: Check if there is exactly one dot in the file name
    if len(parts) != 2:
        return 'No'
    
    # Extract the file name parts
    name_part = parts[0]
    extension_part = parts[1]
    
    # Condition 3: Check the characters before the dot
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Condition 4: Check the extension part
    valid_extensions = ['txt', 'exe', 'dll']
    if extension_part not in valid_extensions:
        return 'No'
    
    return 'Yes'

# Test the function with examples
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'

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
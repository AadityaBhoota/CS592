import re

def file_name_check(file_name):
    # Check for the number of digits in the file's name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Check for the dot separator
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts based on the dot
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'

    # Check the first part (before the dot)
    if not name_parts[0] or not name_parts[0][0].isalpha():
        return 'No'

    # Check the second part (after the dot)
    valid_extensions = ['txt', 'exe', 'dll']
    if name_parts[1] not in valid_extensions:
        return 'No'

    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("image.jpeg"))  # => 'No' (extension not in valid list)
print(file_name_check("file.with.multiple.dots.txt"))  # => 'No' (more than one dot in the file name)
print(file_name_check("file1234.txt"))  # => 'No' (more than three digits in the file name)

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
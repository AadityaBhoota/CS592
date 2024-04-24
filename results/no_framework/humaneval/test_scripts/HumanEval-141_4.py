def file_name_check(file_name):
    # Check condition 1: There should not be more than three digits in the file's name
    if sum(1 for char in file_name if char.isdigit()) > 3:
        return 'No'

    # Check condition 2: The file's name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts: before and after the dot
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'

    name_before_dot, extension = name_parts

    # Check condition 3: The substring before the dot should not be empty and starts with a letter
    if not name_before_dot or not name_before_dot[0].isalpha():
        return 'No'

    # Check condition 4: The substring after the dot should be one of the allowed extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Test the function with examples



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
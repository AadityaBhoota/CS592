def file_name_check(file_name):
    # 1. Check if the file name has more than 3 digits
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # 2. Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # 3. Check if the file name is at least 2 characters long
    if len(file_name) < 2:
        return 'No'
    
    # 4. Check if the substring before the dot starts with a letter
    before_dot, after_dot = file_name.split('.')
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    # 5. Check if the substring after the dot is a valid extension
    valid_extensions = ['txt', 'exe', 'dll']
    if after_dot not in valid_extensions:
        return 'No'
    
    # 6. If all conditions are met, return 'Yes'
    return 'Yes'

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
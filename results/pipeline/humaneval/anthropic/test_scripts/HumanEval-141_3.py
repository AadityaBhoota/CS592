def file_name_check(file_name):
    # Initialize the result
    result = "Yes"

    # Check for more than 3 digits
    if sum(c.isdigit() for c in file_name) > 3:
        result = "No"
        return result

    # Check for exactly one dot
    if file_name.count(".") != 1:
        result = "No"
        return result

    # Split the file name into two parts
    parts = file_name.split(".")
    before_dot, after_dot = parts[0], parts[1]

    # Check if the part before the dot is empty
    if not before_dot:
        result = "No"
        return result

    # Check if the first character of the part before the dot is a letter
    if not before_dot[0].isalpha():
        result = "No"
        return result

    # Check if the part after the dot is a valid extension
    valid_extensions = ["txt", "exe", "dll"]
    if after_dot not in valid_extensions:
        result = "No"
        return result

    return result

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
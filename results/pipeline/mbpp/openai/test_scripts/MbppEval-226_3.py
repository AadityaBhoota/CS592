def odd_values_string(str):
    result = ''  # Step 2: Create an empty string variable to store the result
    
    for i in range(len(str)):  # Step 3: Iterate over the characters in the input string using a loop
        if i % 2 == 0:  # Step 4: Check if the index of the character is even
            result += str[i]  # Step 5: Add the character to the result string
    
    return result  # Step 5: Finally, return the result string

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)
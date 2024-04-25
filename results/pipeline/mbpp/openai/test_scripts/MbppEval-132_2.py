def tup_string(tup1):
    result = ""  # Step 0: Create an empty string
    
    for char in tup1:  # Step 1: Loop through each element in the input tuple
        result += char  # Step 2: Add each element to the string
    
    return result  # Step 3: Return the final string

def check(candidate):
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert tup_string(('p','y','t','h','o','n'))==("python")
    assert tup_string(('p','r','o','g','r','a','m'))==("program")

check(tup_string)
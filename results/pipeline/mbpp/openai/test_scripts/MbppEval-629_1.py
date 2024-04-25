def Split(lst): 
    even_numbers = []  # Step 1: Create an empty list to store even numbers
    
    for num in lst:  # Step 2: Iterate through the input list
        if num % 2 == 0:  # Step 3.1: Check if the number is even
            even_numbers.append(num)  # Step 3.2: Append even numbers to the list

    return even_numbers  # Step 4: Return the list of even numbers

def check(candidate):
    assert Split([1,2,3,4,5]) == [2,4]
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert Split ([8,12,15,19]) == [8,12]

check(Split)
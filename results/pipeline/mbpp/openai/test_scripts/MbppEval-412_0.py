def remove_odd(l):
    even_numbers = []  # Create an empty list to store the even numbers
    
    for num in l:  # Iterate through each number in the input list
        if num % 2 == 0:  # Check if the number is even
            even_numbers.append(num)  # If the number is even, add it to the new list
            
    return even_numbers  # Return the new list containing only even numbers

def check(candidate):
    assert remove_odd([1,2,3]) == [2]
    assert remove_odd([2,4,6]) == [2,4,6]
    assert remove_odd([10,20,3]) == [10,20]

check(remove_odd)
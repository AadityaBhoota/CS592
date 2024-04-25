def bell_number(n):
    bell_numbers = [0] * (n + 1)  # Initialize a list to store the Bell numbers
    bell_numbers[0] = 1  # Set the first Bell number as 1
    
    for i in range(1, n + 1):
        bell_numbers[i] = 0  # Initialize each Bell number as 0
    
    return bell_numbers[n]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)
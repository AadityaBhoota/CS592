def find_Average_Of_Cube(n):
    if n < 1:
        return 0
    
    total = 0
    
    for i in range(1, n+1):
        total += i ** 3
    
    average = total / n
    
    return average

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)
def even_Power_Sum(n): 
    if not isinstance(n, int) or n <= 0:
        return "Please enter a positive integer value for n."
    
    even_numbers = [2*i for i in range(1, n+1)]
    
    fifth_powers = [num**5 for num in even_numbers]
    
    sum_fifth_powers = sum(fifth_powers)

    return sum_fifth_powers

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)
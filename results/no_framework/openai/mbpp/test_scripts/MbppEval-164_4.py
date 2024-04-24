def areEquivalent(num1, num2):
    div_sum1 = sum([i for i in range(1, num1) if num1 % i == 0])
    div_sum2 = sum([i for i in range(1, num2) if num2 % i == 0])
    
    return div_sum1 == div_sum2

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)
def div_sum(n): 
    def get_divisors_sum(x):
        div_sum = 1
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                div_sum += i
                if x // i != i:
                    div_sum += x // i
        return div_sum
    
    x, y = n

    return get_divisors_sum(x) == get_divisors_sum(y)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)
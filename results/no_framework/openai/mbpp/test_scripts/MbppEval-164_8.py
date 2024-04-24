def div_sum(n): 
    def get_divisors_sum(num):
        div_sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i == (num // i):
                    div_sum += i
                else:
                    div_sum += (i + num // i)
        return div_sum

    div_sum_n = get_divisors_sum(n)
    div_sum_n_minus_1 = get_divisors_sum(n - 1)

    return div_sum_n == div_sum_n_minus_1

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)
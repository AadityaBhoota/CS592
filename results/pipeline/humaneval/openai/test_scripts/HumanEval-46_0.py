def fib4(n: int):
    fib4_nums = [0, 0, 2, 0]
    
    for i in range(4, n):
        next_num = sum(fib4_nums)
        fib4_nums.append(next_num)
    
    return fib4_nums[n-1]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)
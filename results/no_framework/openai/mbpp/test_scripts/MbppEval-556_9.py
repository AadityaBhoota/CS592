def find_Odd_Pair(A,N) : 
    count_odd = 0
    count_even = 0

    for i in range(N):
        if A[i] % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return count_even * count_odd

# Test cases




def check(candidate):
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
    assert find_Odd_Pair([1,2,3],3) == 2

check(find_Odd_Pair)
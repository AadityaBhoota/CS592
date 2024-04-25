def find_Odd_Pair(A, N):
    odd_count = 0
    even_count = 0

    for i in range(N):
        if A[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (odd_count * even_count) + (odd_count * (odd_count - 1)) // 2

# Examples




def check(candidate):
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
    assert find_Odd_Pair([1,2,3],3) == 2

check(find_Odd_Pair)
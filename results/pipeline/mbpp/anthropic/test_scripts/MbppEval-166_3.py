def find_even_pair(A):
    even_count = 0
    odd_count = 0
    even_pairs = 0

    # Count even and odd numbers
    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Calculate the number of pairs that XOR to an even number
    for num in A:
        even_pairs += even_count * odd_count
        if num % 2 == 0:
            even_count -= 1
        else:
            odd_count -= 1

    return even_pairs

def check(candidate):
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1

check(find_even_pair)
def get_total_number_of_sequences(m, n):
    def helper(n, start):
        if n == 1:
            return m - start + 1
        
        count = 0
        for i in range(start, m+1):
            count += helper(n-1, i)
        return count
    
    return helper(n, 2)

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)
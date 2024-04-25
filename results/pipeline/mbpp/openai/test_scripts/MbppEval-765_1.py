import math

def is_polite(n):
    k = int(math.log(n, 2))  # Step 0: Find the highest power of 2 that is less than or equal to n
    
    segment_size = 2**k  # Step 1: Calculate the current segment size
    
    offset = n - 2**k  # Step 3: Calculate the offset within the current segment
    
    max_distance = 2**(k-1)  # Step 4: Determine the maximum distance between polite numbers
    
    bottom_boundary = 2**k + 2**(k-1)  # Step 5: Calculate the bottom boundary of the current segment
    
    candidate = bottom_boundary + offset  # Step 6: Calculate the candidate polite number
    
    if candidate > n:  # Step 7: Check if the candidate is greater than n
        return candidate - 2**(k-1)  # Step 8: Return the correct polite number
    else:
        return candidate

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)
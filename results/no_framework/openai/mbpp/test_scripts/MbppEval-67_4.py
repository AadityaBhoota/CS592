def bell_number(n):
    # Initialize the Bell triangle with the first row containing only 1
    bell_triangle = [[1]]

    for i in range(1, n+1):
        new_row = [bell_triangle[i-1][-1]]  # Start the new row with the last element of the previous row
        for j in range(1, i+1):
            new_row.append(new_row[j-1] + bell_triangle[i-1][j-1])  # Sum of last element of the new row and previous row element
        bell_triangle.append(new_row)

    return bell_triangle[n][0]

# Test cases




def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)
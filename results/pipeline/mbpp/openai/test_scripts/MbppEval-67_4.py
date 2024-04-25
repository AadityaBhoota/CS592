def bell_number(n):   
    bell_triangle = [[1]]

    for i in range(1, n):
        row = [bell_triangle[i - 1][0]]

        for j in range(1, i + 1):
            row.append(row[j - 1] + bell_triangle[i - 1][j - 1])

        bell_triangle.append(row)

    return bell_triangle[-1][-1]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)
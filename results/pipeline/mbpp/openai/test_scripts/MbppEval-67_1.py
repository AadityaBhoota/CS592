def bell_number(n):
    bell_triangle = [[1]]

    for i in range(1, n):
        prev_row = bell_triangle[-1]
        new_row = [prev_row[-1]]

        for j in range(i):
            new_row.append(new_row[j] + prev_row[j])

        bell_triangle.append(new_row)

    return bell_triangle[n - 1][0]

def check(candidate):
    assert bell_number(2)==2
    assert bell_number(10)==115975
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300

check(bell_number)
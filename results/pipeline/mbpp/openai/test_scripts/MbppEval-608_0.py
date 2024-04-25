def generate_bell_triangle(rows):
    bell_triangle = [[1]]
    for i in range(1, rows):
        prev_row = bell_triangle[-1]
        current_row = [prev_row[-1]]
        for j in range(i):
            current_row.append(current_row[j] + prev_row[j])
        bell_triangle.append(current_row)
    return bell_triangle

def bell_Number(n):
    triangle = generate_bell_triangle(n)
    return triangle[n - 1][0]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)
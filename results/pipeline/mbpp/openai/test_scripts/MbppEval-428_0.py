def calculate_gap_sequence(n):
    h = 1
    gap_sequence = []
    while h < n / 3:
        h = 3 * h + 1
        gap_sequence.append(h)
    return gap_sequence

def shell_sort(my_list):
    gap_sequence = calculate_gap_sequence(len(my_list))
    
    for h in gap_sequence:
        for i in range(h, len(my_list)):
            temp = my_list[i]
            j = i
            while j >= h and my_list[j - h] > temp:
                my_list[j] = my_list[j - h]
                j -= h
            my_list[j] = temp
    
    return my_list

def check(candidate):
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]

check(shell_sort)
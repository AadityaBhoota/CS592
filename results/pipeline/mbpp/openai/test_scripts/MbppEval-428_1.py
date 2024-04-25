def shell_sort(my_list):
    gap = len(my_list) // 2
    
    while gap > 0:
        for i in range(gap, len(my_list)):
            current_value = my_list[i]
            position = i
            
            while position >= gap and my_list[position - gap] > current_value:
                my_list[position] = my_list[position - gap]
                position = position - gap
            
            my_list[position] = current_value
            
        gap = gap // 2

    return my_list

def check(candidate):
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]

check(shell_sort)
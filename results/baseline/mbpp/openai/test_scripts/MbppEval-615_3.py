def average_tuple(nums):
    averages = []
    
    for tpl in nums:
        tpl_sum = sum(tpl)
        tpl_avg = tpl_sum / len(tpl)
        averages.append(tpl_avg)
    
    return averages

# Test cases




def check(candidate):
    assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
    assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]
    assert average_tuple( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]

check(average_tuple)
def armstrong_number(number):
    sum_of_cubes = 0
    number_str = str(number)
    
    for digit_str in number_str:
        digit = int(digit_str)
        cube = digit ** 3
        sum_of_cubes += cube

    return sum_of_cubes == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)
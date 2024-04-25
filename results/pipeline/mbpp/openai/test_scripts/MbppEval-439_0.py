def multiple_to_single(L):
    # Step 1: Convert each integer to a string
    str_list = [str(num) for num in L]

    # Step 2: Join the strings together
    concatenated_str = ''.join(str_list)

    # Step 3: Convert the concatenated string back to an integer
    single_int = int(concatenated_str)
    return single_int

def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025

check(multiple_to_single)
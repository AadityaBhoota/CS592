def round_and_sum(list1):
    """
    Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.

    Examples:
    round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
    round_and_sum([5,2,9,24.3,29]) == 345
    round_and_sum([25.0,56.7,89.2]) == 513
    """
    rounded_list = [round(num) for num in list1]
    total_sum = sum(rounded_list)
    length = len(list1)
    return total_sum * length

def check(candidate):
    assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
    assert round_and_sum([5,2,9,24.3,29])==345
    assert round_and_sum([25.0,56.7,89.2])==513

check(round_and_sum)
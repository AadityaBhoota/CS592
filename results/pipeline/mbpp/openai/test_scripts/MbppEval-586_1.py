def split_Arr(l, n):
    if n > len(l):
        return "Invalid input: n is greater than the length of the list."

    second_part = l[n:]
    first_part = l[:n]

    return second_part + first_part

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)
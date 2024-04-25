def find_Parity(x):
    if x & 1 == 1:
        return "Odd Parity"
    else:
        return "Even Parity"

def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)
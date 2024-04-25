def find_Parity(x): 
    ''' Finds whether the parity of a given number is odd. '''

    if x % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)
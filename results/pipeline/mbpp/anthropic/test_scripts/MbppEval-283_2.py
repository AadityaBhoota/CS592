def validate(n):
    num_str = str(n)
    freq_dict = {}

    for digit in num_str:
        if digit in freq_dict:
            freq_dict[digit] += 1
        else:
            freq_dict[digit] = 1

    for digit, count in freq_dict.items():
        if count > int(digit):
            return False

    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)
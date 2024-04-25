# Step 0: Define the function is_Diff
def is_Diff(n):
    # Step 1: Separate the odd and even digits of n
    odd_digits = [int(d) for i, d in enumerate(str(n)) if i % 2 != 0]
    even_digits = [int(d) for i, d in enumerate(str(n)) if i % 2 == 0]

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)
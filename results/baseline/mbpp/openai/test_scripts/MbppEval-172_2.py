def count_occurance(s):
    return s.count('std')

# Test the function with the examples



def check(candidate):
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2
    assert count_occurance("stds") == 1
    assert count_occurance("") == 0

check(count_occurance)
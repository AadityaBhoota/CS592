def reverse_string(string):
    return string[::-1]

def reverse_string_list(stringlist):
    return [reverse_string(string) for string in stringlist]

# Test the function with examples




def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)
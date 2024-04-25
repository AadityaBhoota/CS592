def reverse_string_list(stringlist):
    reversed_strings = []

    for string in stringlist:
        reversed_string = string[::-1]
        reversed_strings.append(reversed_string)
    
    return reversed_strings

def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)
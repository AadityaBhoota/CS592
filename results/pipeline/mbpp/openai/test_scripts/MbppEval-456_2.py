def reverse_string_list(stringlist):
    reversed_list = []
    for string in stringlist:
        reversed_string = ''
        for char in string:
            reversed_string = char + reversed_string
        reversed_list.append(reversed_string)
    return reversed_list

def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)
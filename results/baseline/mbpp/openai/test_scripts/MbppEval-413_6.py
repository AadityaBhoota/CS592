def extract_nth_element(list1, n):
    return [x[n] for x in list1]

# Testing the function with provided examples

# Output: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']


# Output: [99, 96, 94, 98]


# Output: [98, 97, 91, 94]
def check(candidate):
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[99, 96, 94, 98]
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],1)==[98, 97, 91, 94]

check(extract_nth_element)
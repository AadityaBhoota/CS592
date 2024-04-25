def sort_sublists(input_list):
    sorted_list = [sorted(sublist, key=lambda x: x.strip().lower()) for sublist in input_list]
    return sorted_list

# Test cases




def check(candidate):
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]

check(sort_sublists)
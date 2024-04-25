def sort_sublists(input_list):
    # Step 0: Define a function named sort_sublists that takes one parameter, input_list
    sorted_list = []
    
    # Step 1: Create an empty list sorted_list to store the sorted sublists
    for sublist in input_list:
        sorted_sublist = sorted(sublist)
        sorted_list.append(sorted_sublist)
    
    return sorted_list

def check(candidate):
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]

check(sort_sublists)
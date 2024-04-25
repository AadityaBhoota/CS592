def sort_sublists(input_list):
    """
    Write a function to sort each sublist of strings in a given list of lists.

    Examples:
    sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"])) == [[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"])) == [['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
    """
    return [sorted(sublist) for sublist in input_list]

def check(candidate):
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]

check(sort_sublists)
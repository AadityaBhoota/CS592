import collections as ct

def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = dict()
    
    for d in [dict1, dict2, dict3]:
        for key, value in d.items():
            merged_dict[key] = value
    
    return merged_dict

# Test the function with the given examples
result1 = merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"O": "Orange", "W": "White", "B": "Black"})


result2 = merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"L": "lavender", "B": "Blue"})


result3 = merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"L": "lavender", "B": "Blue"}, {"G": "Green", "W": "White"})


def check(candidate):
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}

check(merge_dictionaries_three)
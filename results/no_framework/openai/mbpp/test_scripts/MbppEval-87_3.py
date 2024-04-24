def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict()
    
    for d in (dict1, dict2, dict3):
        for key, value in d.items():
            result[key] = value
    
    return result

# Test cases

                                { "G": "Green", "W": "White" },
                                { "O": "Orange", "W": "White", "B": "Black" }))
# Output: {'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}


                                { "G": "Green", "W": "White" },
                                {"L": "lavender", "B": "Blue"}))
# Output: {'R': 'Red', 'B': 'Blue', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'L': 'lavender'}


                                {"L": "lavender", "B": "Blue"},
                                { "G": "Green", "W": "White" }))
# Output: {'R': 'Red', 'B': 'Blue', 'P': 'Pink', 'L': 'lavender', 'G': 'Green', 'W': 'White'}

def check(candidate):
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}

check(merge_dictionaries_three)
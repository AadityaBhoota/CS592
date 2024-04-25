def string_to_tuple(str1):
    char_list = []
    for char in str1:
        char_list.append(char)
    return tuple(char_list)

def check(candidate):
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')

check(string_to_tuple)
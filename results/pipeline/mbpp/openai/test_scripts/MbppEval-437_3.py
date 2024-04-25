def remove_odd(str1):
    result = ""
    
    for index, char in enumerate(str1):
        if index % 2 == 0:
            result += char
            
    return result

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")

check(remove_odd)
def remove_odd(str1):
    result = ""
    
    for i in range(len(str1)):
        char = str1[i]
        if i % 2 == 0:
            result += char
            
    return result

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")

check(remove_odd)
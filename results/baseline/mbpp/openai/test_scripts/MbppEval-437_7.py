def remove_odd(str1):
    return str1[1::2]

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")

check(remove_odd)
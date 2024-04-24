def remove_odd(str1):
    """
    Write a function to remove odd characters in a string.

    Examples:
    remove_odd("python") == ("yhn")
    remove_odd("program") == ("rga")
    remove_odd("language") == ("agae")
    """
    result = ""
    for i, char in enumerate(str1):
        if i % 2 == 0:
            result += char
    return result

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")

check(remove_odd)
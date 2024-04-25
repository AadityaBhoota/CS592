def decode_cyclic(s: str):
    """
    Takes an input string encoded with encode_cyclic function and returns the decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    decoded_groups = [(group[2] + group[:2]) if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)



METADATA = {}


def check(candidate):
    from random import randint, choice
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_cyclic(str)
        assert candidate(encoded_str) == str


check(decode_cyclic)
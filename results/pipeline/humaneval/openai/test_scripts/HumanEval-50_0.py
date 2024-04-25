def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr((ord(ch) - ord("a") - 5) % 26 + ord("a") if ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    decoded_chars = []
    
    for ch in s:
        original_ch = chr((ord(ch) + 5 - ord("a")) % 26 + ord("a") if ch.islower() else ch)
        decoded_chars.append(original_ch)
    
    return "".join(decoded_chars)



METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        assert candidate(copy.deepcopy(encoded_str)) == str


check(decode_shift)
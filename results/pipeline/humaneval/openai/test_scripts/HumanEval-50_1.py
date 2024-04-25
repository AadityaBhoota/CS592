def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([shift_char(ch, 5) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([shift_char(ch, -5) for ch in s])



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
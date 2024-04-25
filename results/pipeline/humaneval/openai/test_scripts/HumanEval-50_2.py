def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decoded_str = ""
    for ch in s:
        if ch.isalpha():
            decoded_char = chr((ord(ch) - ord("a") - 5) % 26 + ord("a"))
            decoded_str += decoded_char
        else:
            decoded_str += ch
    return decoded_str



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
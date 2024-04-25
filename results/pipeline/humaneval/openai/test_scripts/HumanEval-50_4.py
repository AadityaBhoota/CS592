def decode_shift(s: str):
    """
    Decodes a string encoded by shifting every character by 5 in the alphabet.
    """
    decoded_str = "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
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
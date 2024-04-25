def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(i):min((i + 3), len(s))] for i in range(0, len(s), 3)]
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)



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
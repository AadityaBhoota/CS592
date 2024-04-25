def decode_cyclic(s: str):
    groups = [s[i:i+3] for i in range(0, len(s), 3]
    
    decoded_groups = [(group[-1] + group[:2]) if len(group) == 3 else group for group in groups]
    
    decoded_string = "".join(decoded_groups)
    
    return decoded_string



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
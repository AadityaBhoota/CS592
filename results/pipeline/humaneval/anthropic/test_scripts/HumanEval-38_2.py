def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split the input string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Rotate the characters in each group to the right by 1 position
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join all the groups back together to form the final decoded string
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
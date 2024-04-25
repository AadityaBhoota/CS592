def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split the input string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Reverse the cyclic operation for each group to decode it
    decoded_groups = [''.join([group[2], group[0], group[1]]) if len(group) == 3 else group for group in groups]

    # Join the decoded groups to form the decoded string
    decoded_string = ''.join(decoded_groups)
    
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
def decode_cyclic(s: str):
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # Reverse the cyclic shifting for each group
            decoded_group = group[-1] + group[:-1]
            decoded_groups.append(decoded_group)
        else:
            decoded_groups.append(group)
    
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
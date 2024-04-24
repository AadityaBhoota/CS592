def unique(l: list):
    unique_elements = list(set(l))
    unique_elements.sort()
    return unique_elements

# Test the function
if __name__ == "__main__":
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(input_list)
    print(result)



METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)
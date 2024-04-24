from typing import List

def parse_music(music_string: str) -> List[int]:
    beats_mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = music_string.split()
    beats_list = [beats_mapping[note] for note in notes]

    return beats_list

# Test the function with the given example
parsed_notes = parse_music('o o| .| o| o| .| .| .| .| o o')
print(parsed_notes)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('o o o o') == [4, 4, 4, 4]
    assert candidate('.| .| .| .|') == [1, 1, 1, 1]
    assert candidate('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
    assert candidate('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]

check(parse_music)
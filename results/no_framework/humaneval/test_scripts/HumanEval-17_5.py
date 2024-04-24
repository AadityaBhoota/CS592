from typing import List

def parse_music(music_string: str) -> List[int]:
    notes_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    music_notes = music_string.split()
    result = []
    for note in music_notes:
        result.append(notes_duration[note])

    return result

# Test the function with the example provided in the docstring
result = parse_music('o o| .| o| o| .| .| .| .| o o')
print(result)



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
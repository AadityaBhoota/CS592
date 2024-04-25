from typing import List

def parse_music(music_string: str) -> List[int]:
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    result = []
    for note in music_string.split():
        if note in note_values:
            result.append(note_values[note])
    return result



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
from typing import List

def parse_music(music_string: str) -> List[int]:
    note_durations = []
    for char in music_string:
        if char == 'o':
            note_durations.append(4)
        elif char == 'o|':
            note_durations.append(2)
        elif char == '.|':
            note_durations.append(1)
        elif char == ' ':
            pass
    return note_durations



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
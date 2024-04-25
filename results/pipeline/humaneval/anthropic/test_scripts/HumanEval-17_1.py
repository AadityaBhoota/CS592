from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = []
    current_beat = 0
    for char in music_string:
        if char == 'o':
            current_beat = 4
        elif char == '|':
            if current_beat == 4:
                current_beat = 2
            else:
                raise ValueError("Invalid note format: {}".format(music_string))
        elif char == '.':
            current_beat = 1
        elif char == ' ':
            if current_beat > 0:
                beats.append(current_beat)
                current_beat = 0
        else:
            raise ValueError("Invalid character in input string: {}".format(char))
    if current_beat > 0:
        beats.append(current_beat)
    return beats



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
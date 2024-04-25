from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    
    beat_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beat_durations = []
    for note in notes:
        if note in beat_duration:
            beat_durations.append(beat_duration[note])
    
    return beat_durations



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
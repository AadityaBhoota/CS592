from typing import List

def parse_music(music_string: str) -> List[int]:
    durations_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    music_notes = music_string.split()
    return [durations_map[note] for note in music_notes]

# Testing the function with the provided example
result = parse_music('o o| .| o| o| .| .| .| .| o o')




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
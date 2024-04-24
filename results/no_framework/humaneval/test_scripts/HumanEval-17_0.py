from typing import List

def parse_music(music_string: str) -> List[int]:
    # Dictionary to map note symbols to their corresponding beat durations
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the music string by spaces to get individual notes
    notes = music_string.split()
    
    # Map each note to its corresponding beat duration using note_map
    beats = [note_map[note] for note in notes]
    
    return beats

# Testing the function with the provided example
if __name__ == "__main__":
    music_string = 'o o| .| o| o| .| .| .| .| o o'
    result = parse_music(music_string)
    print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]



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
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Define a dictionary to map musical notations to beats
    notation_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music_string by whitespace
    notes = music_string.split()

    # Initialize an empty list to store the number of beats for each note
    beats_list = []

    # Iterate through each note in the notes list
    for note in notes:
        # Map the note to its corresponding number of beats and append to beats_list
        beats_list.append(notation_to_beats.get(note))

    return beats_list

# Test the function with the provided example
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]



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
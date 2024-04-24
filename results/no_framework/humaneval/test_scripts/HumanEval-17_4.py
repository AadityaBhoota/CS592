from typing import List


def parse_music(music_string: str) -> List[int]:
    legend = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    beats_list = [legend[note] for note in music_list]
    return beats_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()



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
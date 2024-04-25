import re

def find_adverb_position(text):
    words = re.findall(r'\w+|\S', text)
    
    for idx, word in enumerate(words):
        if word.endswith("ly"):
            return (text.find(word), text.find(word) + len(word) - 1, word)

# Testing all steps




def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')

check(find_adverb_position)
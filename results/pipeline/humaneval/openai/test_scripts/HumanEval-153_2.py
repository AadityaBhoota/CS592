def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    max_strength = float('-inf')
    
    for extension in extensions:
        CAP = sum(1 for letter in extension if letter.isupper())
        SM = sum(1 for letter in extension if letter.islower())
        strength = CAP - SM
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def check(candidate):

    # Check some simple cases
    assert candidate('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
    assert candidate('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
    assert candidate('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
    assert candidate('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
    assert candidate('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
    assert candidate('YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']) == 'YameRore.okIWILL123'
    assert candidate('finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']) == 'finNNalLLly.WoW'

    # Check some edge cases that are easy to work out by hand.
    assert candidate('_', ['Bb', '91245']) == '_.Bb'
    assert candidate('Sp', ['671235', 'Bb']) == 'Sp.671235'
    

check(Strongest_Extension)
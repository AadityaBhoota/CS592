def Strongest_Extension(class_name, extensions):
    strongest_extension_name = None
    strongest_extension_strength = float('-inf')
    
    for extension in extensions:
        CAP = sum(1 for char in extension if char.isupper())
        SM = sum(1 for char in extension if char.islower())
        extension_strength = CAP - SM
        
        if extension_strength > strongest_extension_strength:
            strongest_extension_name = extension
            strongest_extension_strength = extension_strength
        elif extension_strength == strongest_extension_strength:
            if extensions.index(extension) < extensions.index(strongest_extension_name):
                strongest_extension_name = extension
    
    result = f"{class_name}.{strongest_extension_name}"
    return result

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
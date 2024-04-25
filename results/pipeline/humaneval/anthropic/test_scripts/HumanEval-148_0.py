def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Find the indices of planet1 and planet2
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Create the result list
    result = []
    start = min(index1, index2)
    end = max(index1, index2)
    for i in range(start, end+1):
        result.append(planets[i])
    
    return tuple(sorted(result))

def check(candidate):

    # Check some simple cases
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))      
    assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))  
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))      
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate("Earth", "Earth") == ()
    assert candidate("Mars", "Earth") == ()
    assert candidate("Jupiter", "Makemake") == ()


check(bf)
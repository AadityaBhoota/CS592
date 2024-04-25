def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    
    if i1 < i2:
        return tuple(planets[i1+1:i2])
    else:
        return tuple(planets[i2+1:i1])

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
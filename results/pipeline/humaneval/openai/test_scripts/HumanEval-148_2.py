def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    index1 = planets.index(planet1) if planet1 in planets else -1
    index2 = planets.index(planet2) if planet2 in planets else -1
    
    if index1 == -1 or index2 == -1:
        return ()
    
    if index1 > index2:
        planet1, planet2 = planet2, planet1
        
    between_planets = planets[index1+1:index2]
    
    return tuple(between_planets)

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
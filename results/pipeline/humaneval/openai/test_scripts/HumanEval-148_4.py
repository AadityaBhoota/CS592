def bf(planet1, planet2):
    PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 in PLANETS and planet2 in PLANETS:
        index1 = PLANETS.index(planet1)
        index2 = PLANETS.index(planet2)
        
        if index1 > index2:
            index1, index2 = index2, index1  # Swap the indexes if they are not in the correct order
            
        planets_between = PLANETS[index1+1:index2]
        
        sorted_planets = sorted(planets_between, key=lambda x: PLANETS.index(x))
        
        return tuple(sorted_planets)
        
    else:
        return ()

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
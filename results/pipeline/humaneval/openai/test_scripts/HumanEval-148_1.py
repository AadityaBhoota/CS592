# Step 0: Store the correct planet names in a list in the correct order
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def bf(planet1, planet2):
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index_1 = planets.index(planet1)
    index_2 = planets.index(planet2)
    
    if index_1 == -1 or index_2 == -1:
        return ()
    
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    
    result = planets[index_1+1:index_2]
    result.sort(key=lambda x: planets.index(x))
    
    return tuple(result)

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
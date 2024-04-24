def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    start_index = planets.index(planet1)
    end_index = planets.index(planet2)
    
    if start_index < end_index:
        return tuple(sorted(planets[start_index+1:end_index], key=lambda x: planets.index(x)))
    else:
        return tuple(sorted(planets[end_index+1:start_index], key=lambda x: planets.index(x), reverse=True))

# Test cases
print(bf("Jupiter", "Neptune"))  # Output: ('Saturn', 'Uranus')
print(bf("Earth", "Mercury"))     # Output: ('Venus',)
print(bf("Mercury", "Uranus"))    # Output: ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')

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
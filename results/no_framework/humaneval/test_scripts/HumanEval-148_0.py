def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if planet names are valid
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Find the indexes of planet1 and planet2
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    # Determine the range of planets based on indexes
    start_idx = min(idx1, idx2)
    end_idx = max(idx1, idx2)
    
    # Extract the planets within the range
    result = tuple([planet for planet in planets[start_idx+1:end_idx]])
    
    return result

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
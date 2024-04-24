def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1 not in planets or planet2 not in planets:
        return ()

    start_idx = planets.index(planet1)
    end_idx = planets.index(planet2)

    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx

    return tuple(planets[start_idx+1:end_idx])

# Test cases
print(bf("Jupiter", "Neptune"))  # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))    # ==> ("Venus")
print(bf("Mercury", "Uranus"))   # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

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
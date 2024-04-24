def bf(planet1, planet2):
    # Define the order of planets
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if both planet names are correct
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    
    # Find the indices of the planets in the order list
    idx1 = planets_order.index(planet1)
    idx2 = planets_order.index(planet2)
    
    # Determine the start and end indices for slicing the list
    start_idx = min(idx1, idx2) + 1
    end_idx = max(idx1, idx2)
    
    # Extract the planets between the orbit of planet1 and planet2
    result = tuple(planets_order[start_idx:end_idx])
    
    return result

# Test the function with the provided examples
print(bf("Jupiter", "Neptune"))  # Output: ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))     # Output: ("Venus")
print(bf("Mercury", "Uranus"))    # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

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
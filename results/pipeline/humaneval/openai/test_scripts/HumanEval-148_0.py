planet_order = {
    "Mercury": 1,
    "Venus": 2,
    "Earth": 3,
    "Mars": 4,
    "Jupiter": 5,
    "Saturn": 6,
    "Uranus": 7,
    "Neptune": 8
}

def bf(planet1, planet2):
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()

    order_planet1 = planet_order[planet1]
    order_planet2 = planet_order[planet2]

    planets_between = [planet for planet, order in planet_order.items()
                       if order_planet1 <= order <= order_planet2]

    if not planets_between:
        return ()

    sorted_planets = sorted(planets_between, key=lambda x: planet_order[x])

    return tuple(sorted_planets)

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
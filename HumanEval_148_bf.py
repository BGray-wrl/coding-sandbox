def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
        
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    start_index = min(index1, index2)
    end_index = max(index1, index2)
    
    return tuple(planets[start_index + 1 : end_index])
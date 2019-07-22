class System:

    bodies = []

    def __init__(self):
        pass
    
    def add (self, new_body):
        self.bodies.append(new_body)

    def total_mass(self):
        total_mass = 0
        for curr_body in self.bodies:
            total_mass += curr_body.mass
        return total_mass
    
class Body:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = day  

class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet 


body1 = Body("Sun", 1.989 * (10)**30)
body2 = Body("Earth", 5.972 * (10)**24)
planetEarth = Planet(body2.name, body2.mass, 1, 365)
moon1 = Moon(planetEarth.name, planetEarth.mass, 27, planetEarth)

import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def main(self):
        s = Sphere()
        print("Radius of the sphere: ", s.get_radius())
        print("Surface area: ", s.surface_area())
        print("Volume: ", s.volume())

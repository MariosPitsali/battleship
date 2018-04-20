class Ship(object):
    
    def __init__(self, name, hit_points):
        self.name = name
        self._hit_points = hit_points
    
    def damage(self, damage):
        self._hit_points -= damage
        if self._hit_points == 0:
            print ("The {} is destroyed".format(self.name))
        else:
            print ("The {0.name} has {0._hit_points} spaces left".format(self))
    
class Carrier(Ship):
    
    def __init__(self, name):
        super(Carrier, self).__init__(name = name, hit_points = 5)
    
class Battleship(Ship):
    
    def __init__(self, name):
        super(Battleship, self).__init__(name = name, hit_points = 4)

class Cruiser(Ship):
    
    def __init__(self, name = "Cruiser"):
        super().__init__(name =  name, hit_points = 3)


class Submarine(Ship):
    
    def __init__(self):
        super().__init__(name = "Submarine", hit_points = 3)

class Destroyer(Ship):
    
    def __init__(self):
        super().__init__(name = "Destroyer", hit_points = 2)
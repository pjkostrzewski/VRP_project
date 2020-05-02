import math


class Point(object):
    
    number_of_points = 0
    def __init__(self, id_number: int, xy: tuple):
        self._id_number = id_number
        self._x = xy[0]
        self._y = xy[1]
        Point.number_of_points += 1
    
    def __str__(self):
        return "({},{})".format(self._x, self._y)
    
    def __repr__(self):
        return "POINT({},{})".format(self._x, self._y)
    
    def __hash__(self):
        return int(self.x*10 + self.y)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    @property
    def id_number(self):
        return self._id_number 
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    def get_distance_to(self, point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

class Point(object):
    
    number_of_points = 0
    def __init__(self, xy: tuple, demand: int):
        self._x = xy[0]
        self._y = xy[1]
        self._demand = demand
        Point.number_of_points += 1
    
    def __str__(self):
        return "({},{}) - {}".format(self._x, self._y, self._demand)
    
    def __repr__(self):
        return "({},{}) - {}".format(self._x, self._y, self._demand)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def demand(self):
        return self._demand
    
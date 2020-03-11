from Route import Route
import helpers


class RoutesContainer(object):
    
    salesmen = helpers.salesmen
    
    def __init__(self, routes=None):
        if routes:
            self.routes = routes
        else:
            self.routes = []
    
    def calculate_distance(self):
        distance = 0
        for route in self.routes:
            distance += route.calculate_distance()
        return distance
    
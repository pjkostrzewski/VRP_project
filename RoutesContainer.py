from random import sample
from Route import Route
import helpers
from copy import deepcopy


class RoutesContainer(object):
    
    salesmen = helpers.salesmen
    depot =  None
    points = None
    
    def __init__(self, routes=None, details=None):
        if routes and details:
            self.routes = routes
            self.details = details
        else:
            self.routes = []
            self.details = []
            
    def calculate_distance(self):  # change!
        distance = 0
        previous_idx = 0
        for detail_idx in self.details:
            temp_route = Route(self.routes[previous_idx:detail_idx])
            distance += temp_route.calculate_distance()
            previous_idx = detail_idx
        return distance
    
    def uniques_only(self):
        raise NotImplementedError
    
    @classmethod
    def set_depot(cls, point):
        cls.depot = point
    
    @classmethod
    def set_points(cls, points):
        cls.points = points
    
def generate_random_routes_container(points):  # Done
    return sample(points, len(points))

def generate_random_details(points):  # Done
    result = []
    parts = helpers.salesmen
    generated = [0] + sorted(sample(range(1,len(points)), parts-1)) + [len(points)]
    for idx in range(1, len(generated)):
        result.append(generated[idx]-generated[idx-1])
    return result
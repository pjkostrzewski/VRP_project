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
            
    def calculate_distance(self):
        distance = 0
        previous_idx = 0
        for detail_idx in sorted(self.details + [len(self.points)]):
            temp_route = Route(self.routes[previous_idx:detail_idx])
            distance += temp_route.calculate_distance()
            previous_idx = detail_idx
            
        return distance
    
    def uniques_only(self):
        return len(set(self.routes.route)) == len(self.routes.route)
    
    @classmethod
    def set_depot(cls, point):
        cls.depot = point
    
    @classmethod
    def set_points(cls, points):
        cls.points = points

    def get_subroutes(self):
        subroutes = []
        copy_routes = deepcopy(self.routes)
        for nodes in self.details:
            to_add = copy_routes[:nodes]
            del copy_routes[:nodes]
            subroutes.append(Route(to_add))
        return subroutes
        
def generate_random_routes_container(points):
    sam = Route(sample(points, len(points)))
    details = generate_random_details(points)
    return RoutesContainer(sam, details)

def generate_random_details(points):
    result = []
    while True:
        result.clear()
        parts = helpers.salesmen
        generated = [0] + sorted(sample(range(2,len(points)-2), parts-1)) + [len(points)]
        for idx in range(1, len(generated)):
            result.append(generated[idx]-generated[idx-1])
        if 1 not in result:
            break
    return result


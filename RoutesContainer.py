from random import sample
from Route import Route
import helpers
from copy import deepcopy


class RoutesContainer(object):
    
    salesmen = helpers.salesmen
    depot =  None
    points = None
    
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
    
    def uniques_only(self):
        raise NotImplementedError
    
    @classmethod
    def set_depot(cls, point):
        cls.depot = point
    
    @classmethod
    def set_points(cls, points):
        cls.points = points
    
def generate_random_routes_container(points):
    RoutesContainer.set_points(points)
    nodes = deepcopy(points)
    number_of_nodes = int(round(len(points)/helpers.salesmen))
    results = []
    
    def clear_sample():
        for point in route:
            nodes.remove(point)
            
    while True:
        try:
            route = sample(nodes, number_of_nodes)
            clear_sample()
            if len(nodes) == 0:
                break
        except ValueError:
            route = nodes
            break
        finally:
            results.append(Route(route))
    assert len(results) == helpers.salesmen, "size of results is wrong"
    return RoutesContainer(results)
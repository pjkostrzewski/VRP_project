from random import sample
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
    
    
def generate_random_routes_container(points):
    number_of_nodes = int(round(len(points)/helpers.salesmen))
    results = []
    
    def clear_sample():
        for point in route:
            points.remove(point)
            
    while True:
        try:
            route = sample(points, number_of_nodes)
            clear_sample()
            if len(points) == 0:
                break
        except ValueError:
            route = points
            break
        finally:
            results.append(Route(route))
    assert len(results) == helpers.salesmen, "size of results is wrong"
    return RoutesContainer(results)
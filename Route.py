from Coord import Point


class Route(object):
    
    number_of_all_routes = 0
    
    def __init__(self, id_number, route):
        self.id_number = id_number
        self.route = route
        
        Route.number_of_all_routes += 1
        
    def get_length(self):
        return len(self.route)
    
    def get_distance(self):
        return -1
    
    def get_fitness(self):
        distance = self.get_distance()
        return 1/distance
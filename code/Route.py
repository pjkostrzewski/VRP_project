from Coord import Point
import helpers
import math


class Route(object):
    
    number_of_all_routes = 0
    depot = helpers.depot
    
    def __init__(self, points=None):
        Route.number_of_all_routes += 1
        
        self.id_number = self.number_of_all_routes
        self.route = points if points else []
        self.distance = self.calculate_distance()
        # self.fitness = 1/self.distance
        
    def __repr__(self):
        return "Route {}".format(self.id_number)
    
    def __eq__(self, other):
        return self.route == other.route
    
    def __getitem__(self, idx):
        return self.route[idx]
    
    def __setitem__(self, idx, value):
        self.route[idx] = value
    
    def __index__(self):
        return bool(self.route)
    
    def __len__(self):
        return len(self.route)
    
    def __delitem__(self, item):
        del self.route[item]
    
    def get_full_route(self):
        return [self.depot] + self.route + [self.depot]
    
    def get(self):
        return self.route
    
    def get_length(self):
        return len(self.route)
    
    def get_paired_points(self):
        full_route = self.get_full_route()
        return [(full_route[i], full_route[i+1]) for i in range(len(full_route)-1)]
    
    def uniques_only(self):
        return len(set(self.route)) == len(self.route)
    
    @staticmethod
    def get_distance_between_points(a: Point, b: Point):
        return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)        
        
    def calculate_distance(self):
        distance = 0
        paired_points = self.get_paired_points()
        for x, y in paired_points:
            distance += self.get_distance_between_points(x, y)
        return distance
    
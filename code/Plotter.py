import matplotlib.pyplot as plt
from RoutesContainer import RoutesContainer
from Route import Route


class MatplotlibPlotter(object):
    depot_color = '#ff0000'
     
    def __init__(self):
        self.fig = plt.figure()
    
    def draw_points(self, points):
        x_values = [point.x for point in points]
        y_values = [point.y for point in points]
        plt.scatter(x_values, y_values)   
    
    def draw_depot(self, depot):
        plt.scatter(depot.x, depot.y, c=self.depot_color, s=50)
    
    def draw_route(self, route):
        print('draw route', route)
        x_route = [point.x for point in route]
        y_route = [point.y for point in route]
        plt.plot(x_route, y_route)
    
    def draw(self, routes_container):
        assert isinstance(routes_container, RoutesContainer)
        self.draw_depot(RoutesContainer.depot)
        self.draw_points(RoutesContainer.points)  
        previous = 0
        # if len(routes_container.details) == 1:
        #     detail = 
        #     self.draw_route(Route(routes_container.routes[:detail]).get_full_route())
        #     self.draw_route(Route(routes_container.routes[detail:]).get_full_route())
        for detail in routes_container.details:
            print(routes_container.routes[previous:previous+detail])
            self.draw_route(Route(routes_container.routes[previous:previous+detail]).get_full_route())
            previous += detail

        
    @staticmethod
    def show():
        plt.show()
    
    @staticmethod
    def ion():
        plt.ion()
    
    @staticmethod
    def pause(timeout=0.01):
        plt.pause(timeout)
        
    def clear(self):
        self.fig.clear()
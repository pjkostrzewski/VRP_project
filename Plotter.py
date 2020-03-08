import matplotlib.pyplot as plt


class MatplotlibPlotter(object):
    depot_color = '#ff0000'
    
    
    def __init__(self):
        self.fig = plt.figure()
    
    def draw_points(self, points):
        x_values = [point.x for point in points]
        y_values = [point.y for point in points]
        depot = x_values[0], y_values[0]
        plt.scatter(*depot, c=self.depot_color, s=50)
        plt.scatter(x_values[1:], y_values[1:])   
    
    def draw_routes(self, points, route):
        x_route = [point.x for point in route]
        y_route = [point.y for point in route]
        plt.plot(x_route, y_route)
    
    def draw(self, points, routes):
        self.draw_points(points)
        self.draw_routes(points, routes)
        
    @staticmethod
    def show():
        plt.show()
    
    @staticmethod
    def ion():
        plt.ion()
    
    @staticmethod
    def pause():
        plt.pause(0.01)
        
    def clear(self):
        self.fig.clear()
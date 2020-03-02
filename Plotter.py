import matplotlib.pyplot as plt


class MatplotlibPlotter(object):
    depot_color = '#ff0000'
    
    
    def __init__(self):
        pass
    
    def draw_points(self, points):
        x_values = [point.x for point in points]
        y_values = [point.y for point in points]
        depot = x_values[0], y_values[0]
        plt.scatter(*depot, c=self.depot_color, s=50)
        plt.scatter(x_values[1:], y_values[1:])   
    
    def draw_routes(self, routes, points):
        for route in routes:
            x_route = [points[point-1].x for point in route]
            y_route = [points[point-1].y for point in route]
            plt.plot(x_route, y_route)
    
    @staticmethod
    def show():
        plt.show()
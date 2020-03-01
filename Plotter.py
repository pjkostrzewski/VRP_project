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
        depot = points[0].x, points[0].y
        for route in routes:
            print(route)
            x_route = [depot[0]] + [points[point].x for point in route] + [depot[0]]
            y_route = [depot[1]] + [points[point].y for point in route] + [depot[1]]
            plt.plot(x_route, y_route)
    
    @staticmethod
    def show():
        plt.show()
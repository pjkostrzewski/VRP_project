import random
from Coord import Point
from Route import Route
from RoutesContainer import RoutesContainer
from clockwise import clockwise
from Plotter import MatplotlibPlotter

def random_ints_with_sum(n):
    """
    Generate non-negative random integers summing to `n`.
    """
    while n > 0:
        r = random.randint(0, n)
        yield r
        n -= r

points = clockwise("eil51/moje8_m2.tsp")
all_points = []
for idx, p in enumerate(points):
    temp = Point(idx, tuple(p))
    all_points.append(temp)
route = Route(all_points)
container = RoutesContainer(routes=route, details=[5,6])
container.set_points(all_points)
container.set_depot(Point(-1, (20,20)))
print(container.calculate_distance())
plotter = MatplotlibPlotter()
plotter.draw(container)
plotter.show()
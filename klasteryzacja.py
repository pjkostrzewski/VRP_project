import random
from Coord import Point
from Route import Route
from RoutesContainer import RoutesContainer
from clustering import clustering
from Plotter import MatplotlibPlotter

def klasteryzacja():
    x_points, y_points, details = clustering()
    all_points = []
    for idx, xy in enumerate(zip(x_points, y_points)):
        point = Point(idx+1, tuple(xy))
        all_points.append(point)
    return all_points, details
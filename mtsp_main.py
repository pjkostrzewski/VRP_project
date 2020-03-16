from random import sample
from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, FirstPopulation, ChildsPopulation
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import RoutesContainer


def generate_random_routes_container(salesmen, points):
    number_of_nodes = int(round(len(points)/salesmen))
    results = []
    
    def clear_sample():
        for point in route:
            points.remove(point)
            
    while True:
        try:
            route = sample(points, number_of_nodes)
            clear_sample()
        except ValueError:
            route = points
            break
        finally:
            results.append(Route(route))
            
    return RoutesContainer(results)

benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m2-tours.txt")

plotter = MatplotlibPlotter()
points = benchmark.get_points()
population = FirstPopulation(points)
print(len(points[1:]))
routes_container = generate_random_routes_container(4, points[1:])
# routes_container = RoutesContainer([route1, route2])
# print(routes_container.calculate_distance())
plotter.draw(points, routes_container)
plotter.show()

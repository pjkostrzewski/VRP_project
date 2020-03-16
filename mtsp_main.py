from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, FirstPopulation, ChildsPopulation
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import generate_random_routes_container


benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m2-tours.txt")

plotter = MatplotlibPlotter()
points = benchmark.get_points()
# population = FirstPopulation(points)
routes_container = generate_random_routes_container(points[1:])
# routes_container = RoutesContainer([route1, route2])
# print(routes_container.calculate_distance())
plotter.draw(points, routes_container)
plotter.show()

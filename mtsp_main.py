from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, FirstPopulation, ChildsPopulation
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import RoutesContainer


salesmen = 2
benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m{}-tours.txt".format(salesmen))

plotter = MatplotlibPlotter()

points = benchmark.get_points()
route0 = Route(points)
print(route0.calculate_distance())
route1 = Route(points[1:4])
route2 = Route(points[4:9])
route3 = Route(points[9:])
# routes = benchmark.get_routes()
routes_container = RoutesContainer([route1, route2, route3])
print(routes_container.calculate_distance())
plotter.draw(points, routes_container)
plotter.show()

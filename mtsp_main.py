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
Population.configure(points)
# routes_container = generate_random_routes_container(points)
first = FirstPopulation()
print(first.points)
best = first.get_fittest_route()
# print(first.get_population())
plotter.draw(best)
plotter.show()

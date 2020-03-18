from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, create_random_population
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import generate_random_routes_container


benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m2-tours.txt")

plotter = MatplotlibPlotter()
points = benchmark.get_points()
Population.configure(points)
# routes_container = generate_random_routes_container(points)
first = create_random_population()
print(first)
best = first.get_fittest_container()
print(best)
# print(first.get())
plotter.draw(best)
plotter.show()

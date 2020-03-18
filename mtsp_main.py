from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, create_random_population
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import generate_random_routes_container


benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m2-tours.txt")

Population.configure(benchmark)
plotter = MatplotlibPlotter()

first = create_random_population()
second = Population(first)
best0 = first.get_fittest_container()
best = second.get_fittest_container()
plotter.draw(best)

plotter.show()

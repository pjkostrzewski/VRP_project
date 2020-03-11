from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, FirstPopulation, ChildsPopulation
from GA import GeneticAlgorithm


salesmen = 2
benchmark = Benchmark(  vrp_path="eil51/eil51.tsp", 
                        solution_path="eil51/moje8_m{}-tours.txt".format(salesmen))

plotter = MatplotlibPlotter()

points = benchmark.get_points()
routes = benchmark.get_routes()

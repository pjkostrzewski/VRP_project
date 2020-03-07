from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import FirstPopulation, ChildsPopulation


salesmen = 2
benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m{}-tours.txt".format(salesmen))
points = benchmark.get_points()
routes = benchmark.get_routes()
first = FirstPopulation(points)
print(first.get_population())
first.crossover_population()
first.mutate_population()
print(first.get_population())

# plotter = MatplotlibPlotter()
# plotter.draw(points, routes)
# plotter.show()




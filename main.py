from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter

salesmen = 2
benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m{}-tours.txt".format(salesmen))
points = benchmark.get_points()
routes = benchmark.get_routes()
print(benchmark.get_cost())
plotter = MatplotlibPlotter()
plotter.draw(points, routes)
plotter.show()


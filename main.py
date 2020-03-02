from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter

salesmen = 7
benchmark = Benchmark(  vrp_path="eil51/eil51.tsp", 
                        solution_path="eil51/eil51(m={})-tours.txt".format(salesmen))
points = benchmark.get_points()
routes = benchmark.get_routes()
plotter = MatplotlibPlotter()
plotter.draw(points, routes)
plotter.show()


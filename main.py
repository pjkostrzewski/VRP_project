from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, FirstPopulation, ChildsPopulation


salesmen = 2
benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m{}-tours.txt".format(salesmen))

plotter = MatplotlibPlotter()

points = benchmark.get_points()
routes = benchmark.get_routes()

population = None
running = True
best = None
same = 0
while running and same < 1000:
    plotter.ion()
    if population is None:
        population = FirstPopulation(points)
    else:
        previous_population = population.get_population()
        population = ChildsPopulation(previous_population)
    population.crossover_population()
    population.mutate_population()
    fittest_route = population.get_fittest_route()
    
    if best is None:
        best = fittest_route
    elif fittest_route.calculate_distance() < best.calculate_distance():
        best = fittest_route
        plotter.clear()
        plotter.draw(points, best.get_full_route())
        same = 0
    else:
        same += 1
    print(Population.number_of_populations, best.calculate_distance())
    plotter.show()
    plotter.pause()
    
plotter.draw(points, best.get_full_route())
print(best.get_full_route())
print(best.calculate_distance())
plotter.show()
    





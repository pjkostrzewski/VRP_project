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
while running and Population.number_of_populations < 100:
    if population is None:
        population = FirstPopulation(points)
    else:
        previous_population = population.get_population()
        population = ChildsPopulation(previous_population)
    population.crossover_population()
    population.mutate_population()
    fittest_route = population.get_fittest_route()
    print(Population.number_of_populations,fittest_route.distance)
    if best is None:
        best = fittest_route
    elif fittest_route.distance < best.distance:
        best = fittest_route

    plotter.ion()
    plotter.clear()
    plotter.draw(points, best.get_full_route())
    print(best.distance)
    plotter.show()
    plotter.pause()
    
    





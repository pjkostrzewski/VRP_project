from BenchmarksUtils import Benchmark
from Plotter import MatplotlibPlotter
from Population import Population, create_random_population
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import RoutesContainer, generate_random_routes_container


benchmark = Benchmark(  vrp_path="eil51/moje8_m2.tsp", 
                        solution_path="eil51/moje8_m2-tours.txt")

Population.configure(benchmark)
plotter = MatplotlibPlotter()


running = True
same = 0
population = None
best = None
while running and same < 1000:
    same += 1
    print(same, Population.number_of_populations)
    plotter.ion()
    if population is None:
        population = create_random_population()
    else:
        previous_population = population.get()
        population = Population(previous_population)
    population.crossover_population()
    population.mutate_population()
    fittest = population.get_fittest_container()
    if best is None:
        best = fittest
    elif fittest.calculate_distance() < best.calculate_distance():
        print("================================================")
        best = fittest
        plotter.clear()
        plotter.draw(best)
        # same = 0
        print(Population.number_of_populations, best.calculate_distance())  
    plotter.show()
    plotter.pause()
print(best.calculate_distance())
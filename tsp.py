import random

cities = [2, 3, 4, 5, 6, 7]

population_size = 30
mutation_rate = 0.3
crossover_rate = 0.5

def create_population():
    population = []
    for _ in range(population_size):
        population.append(random.sample(cities, len(cities)))
    return population


def crossover(first, second):
    if random.random() <= crossover_rate:
        size = len(first)
        pivot = random.randint(1,size-2)
        left = first[:pivot] + second[pivot:]
        right = first[pivot:] + second[:pivot]
        return left, right
    else:
        return first, second

after_crossover = []

def add_to_results(route):
    if len(set(route)) == len(route) and route not in after_crossover:
        after_crossover.append(route)


def mutation(route):
    if random.random() <= mutation_rate:
        l,r = random.sample(range(len(route)), 2)
        l_value = route[l]
        r_value = route[r]
        route[l], route[r] = r_value, l_value
    
population = create_population() 
print(population)
c = 1
while len(after_crossover) < population_size:
    first = random.choice(population)
    second = random.choice(population)
    left, right = crossover(first, second)
    mutation(left)
    mutation(right)
    add_to_results(left)
    add_to_results(right)
    c+=1
print("operation takes {} moves.".format(c))
print(after_crossover)
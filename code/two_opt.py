"""

repeat until no improvement is made {
    start_again:
    best_distance = calculateTotalDistance(existing_route)
    for (i = 1; i <= number of nodes eligible to be swapped - 1; i++) {
        for (k = i + 1; k <= number of nodes eligible to be swapped; k++) {
            new_route = 2optSwap(existing_route, i, k)
            new_distance = calculateTotalDistance(new_route)
            if (new_distance < best_distance) {
                existing_route = new_route
                best_distance = new_distance
                goto start_again
            }
        }
    }
}

procedure 2optSwap(route, i, k) {
    1. take route[0] to route[i-1] and add them in order to new_route
    2. take route[i] to route[k] and add them in reverse order to new_route
    3. take route[k+1] to end and add them in order to new_route
    return new_route;
}

"""
from copy import deepcopy
from Route import Route


def two_opt_swap(route: Route, i, k):
    route = route.route
    part_1 = deepcopy(route[0:i])
    part_2 = deepcopy(route[i:k])
    part_2.reverse()
    part_3 = deepcopy(route[k:])
    return Route(part_1 + part_2 + part_3)


def two_opt_algorithm(route: Route, stop_value=1000):
    no_changes = 0
    nodes = len(route)
    while no_changes <= stop_value:
        best_distance = route.calculate_distance()
        for i in range(nodes-1):
            for k in range(i+1, nodes):
                new_route = two_opt_swap(route, i, k)
                new_distance = new_route.calculate_distance()
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
                    no_changes = 0
                else:
                    no_changes += 1
    return route

def two_opt_for_route_container(route_container):
    new_routes = []
    for r in route_container.get_subroutes():
        if len(r.route) > 2:
            res = two_opt_algorithm(r)
        else: 
            res = r
        for point in res:
            new_routes.append(point)
    route_container.routes.route = new_routes 
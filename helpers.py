from Coord import Point


population_size = 100
depot = Point(-1, (20, 20))  # 37, 52
tournament_size = 6
salesmen = 2

def det_matrix(a, b, c):
    return a.x*b.y+b.x*c.y+c.x*a.y-c.x*b.y-a.x*c.y-b.x*a.y


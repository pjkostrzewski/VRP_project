import re
from Coord import Point

class BenchmarkBase(object):
    
    def get_vrp_data(self, path: str):
        with open(path, "r") as f:
            data = f.read()
        return data  
    
    @staticmethod
    def str_to_ints_in_tuple(arg: str) -> tuple:
        return tuple(map(int, arg.split(" ")))
    
class BenchmarkCaseParser(BenchmarkBase):
    
    def __init__(self, vrp_path):
        self.vrp_data = self.get_vrp_data(vrp_path)
    
    def get_name(self) -> str:
        return re.findall(r'NAME : (.*)', self.vrp_data)[0]
        
    def get_capacity(self) -> int:
        return int(re.findall(r'CAPACITY : (.*)', self.vrp_data)[0])
    
    def get_coords(self) -> list:
        coords = re.findall(r' \d{1,3} (\d{1,3} \d{1,3})\n', self.vrp_data)
        return [self.str_to_ints_in_tuple(coord) for coord in coords]
    
    def get_demands(self) -> list:
        demands = re.findall(r'\n\d{1,3} (\d{1,3})', self.vrp_data)
        return list(map(int, demands))
    
    def get_points(self) -> list:
        points = []
        coords = self.get_coords()
        demands = self.get_demands()
        count = 1
        for xy, demand in zip(coords, demands):
            points.append(Point(id_number=count, xy=xy, demand=demand))
            count += 1
        return points
    
class BenchmarkSolutionParser(BenchmarkBase):
    
    def __init__(self, solution_path):
        self.solution_data = self.get_vrp_data(solution_path)

    def get_cost(self) -> int:
        return int(re.findall(r'cost (.*)', self.solution_data)[0])
    
    def get_routes(self) -> list:
        routes = re.findall(r'Route #\d{1,3}: (.*)', self.solution_data)
        return [self.str_to_ints_in_tuple(route) for route in routes]
        

class Benchmark(object):
    def __init__(self, vrp_path: str, solution_path: str):
        
        self._case_parser = BenchmarkCaseParser(vrp_path)
        self._solution_parser = BenchmarkSolutionParser(solution_path)

    def get_points(self) -> list:
        return self._case_parser.get_points()
    
    def get_routes(self) -> list:
        return self._solution_parser.get_routes()
    
    def get_cost(self) -> int:
        return self._solution_parser.get_cost()
        
import re
from Coord import Point

class BenchmarkBase(object):
    
    def get_vrp_data(self, path: str):
        with open(path, "r") as f:
            data = f.read()
        return data  
    
    @staticmethod
    def str_to_ints_in_tuple(arg: str) -> tuple:
        return tuple(map(int, arg.strip().split(" ")))
    
class BenchmarkCaseParser(BenchmarkBase):
    
    def __init__(self, vrp_path):
        self.vrp_data = self.get_vrp_data(vrp_path)
    
    def get_name(self) -> str:
        return re.findall(r'NAME : (.*)', self.vrp_data)[0]
        
    def get_dimension(self) -> int:
        return int(re.findall(r'DIMENSION : (.*)', self.vrp_data)[0])
    
    def get_coords(self) -> list:
        coords = re.findall(r'\d{1,3} (\d{1,3} \d{1,3})\n', self.vrp_data)
        return [self.str_to_ints_in_tuple(coord) for coord in coords]
    
    def get_points(self) -> list:
        points = []
        coords = self.get_coords()
        for id_number, coord in enumerate(coords):
            points.append(Point(id_number=id_number+1, xy=coord))
        return points
    
class BenchmarkSolutionParser(BenchmarkBase):
    
    def __init__(self, solution_path):
        self.solution_data = self.get_vrp_data(solution_path)

    def get_cost(self) -> float:
        return float(re.findall(r'Cost: (.*)', self.solution_data)[0])
    
    def get_routes(self) -> list:
        routes = re.findall(r'(1 .* 1 )', self.solution_data)
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
        
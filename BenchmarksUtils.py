import re


class BenchmarkCaseParser(object):
    
    def __init__(self, vrp_path):
        self.vrp_data = self._get_vrp_data(vrp_path)
    
    def get_name(self) -> str:
        return re.findall(r'NAME : (.*)', self.vrp_data)[0]
        
    def get_capacity(self) -> int:
        return int(re.findall(r'CAPACITY : (.*)', self.vrp_data)[0])
    
    def get_coords(self):
        s2t = lambda x: tuple(map(int, x.split(" ")))  # string to coords format (int, int)
        coords = re.findall(r' \d{1,3} (\d{1,3} \d{1,3})\n', self.vrp_data)
        return [s2t(coord) for coord in coords]
    
    def get_demands(self):
        demands = re.findall(r'\n\d{1,3} (\d{1,3})', self.vrp_data)
        return list(map(int, demands))
    
    def _get_vrp_data(self, vrp_path):
        with open(vrp_path, "r") as f:
            data = f.read()
        return data
    
    
class BenchmarkSolutionParser(object):
    
    def __init__(self, solution_path):
        self.solution_data = self._get_solution_data()

    def get_cost(self):
        raise NotImplementedError
    
    def get_routes(self):
        raise NotImplementedError
    
    def _get_solution_data(self):
        raise NotImplementedError
    
a = BenchmarkCaseParser("/Users/patrykkostrzewski/Projects/VRP_project/A-VRP/A-n32-k5.vrp")
print(a.get_name())
print(a.get_capacity())
print(a.get_coords())
print(a.get_demands())
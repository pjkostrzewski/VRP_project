from Route import Route
import helpers


class RoutesContainer(object):
    
    salesmen = helpers.salesmen
    
    def __init__(self, routes=None):
        if routes:
            self.routes = routes
        else:
            self.routes = []
    
        
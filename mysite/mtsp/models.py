from django.db import models
import math


class Coord(models.Model):
    id_number = models.IntegerField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()
    
    def get_distance_to(self, point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    
    
import pytest
from VRP_project.code.Coord import Point


def test_create_point():
    point = Point(-1, (20,5))
    assert point.x == 20 and point.y == 5   
    
def test_calculate_distance():
    a = Point(1, (20,5))
    b = Point(2, (23,9))
    c = Point(3, (30,5))
    print(a.get_distance_to(b))
    assert a.get_distance_to(b) == 5 and a.get_distance_to(c) == 10
    
def test_id_number():
    point = Point(10, (20,20))
    assert point.id_number == 10

def test_str_point():
    point = Point(10, (20,20))
    assert str(point) == "(20,20)"
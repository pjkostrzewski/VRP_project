from Coord import Point
  
# Given three colinear points p, q, r, the function checks if  
# point q lies on line segment 'pr'  
def on_segment(p, q, r): 
    return ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y)))
  
def orientation(p, q, r): 
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
        return 1
    elif (val < 0): 
        return 2
    else: 
        return 0

def do_intersect(p1,q1,p2,q2): 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    if (o1 != o2) and (o3 != o4): 
        return True
  
    elif ((o1 == 0) and on_segment(p1, p2, q1)): 
        return True
  
    elif ((o2 == 0) and on_segment(p1, q2, q1)): 
        return True
  
    elif ((o3 == 0) and on_segment(p2, p1, q2)): 
        return True
  
    elif ((o4 == 0) and on_segment(p2, q1, q2)): 
        return True
  
    return False
  
# # Driver program to test above functions: 
# p1 = Point((1, 1)) 
# q1 = Point(10, 1) 
# p2 = Point(1, 2) 
# q2 = Point(10, 2) 
  
# if doIntersect(p1, q1, p2, q2): 
#     print("Yes") 
# else: 
#     print("No") 
  
# p1 = Point(10, 0) 
# q1 = Point(0, 10) 
# p2 = Point(0, 0) 
# q2 = Point(10,10) 
  
# if doIntersect(p1, q1, p2, q2): 
#     print("Yes") 
# else: 
#     print("No") 
  
# p1 = Point(-5,-5) 
# q1 = Point(0, 0) 
# p2 = Point(1, 1) 
# q2 = Point(10, 10) 
  
# if doIntersect(p1, q1, p2, q2): 
#     print("Yes") 
# else: 
#     print("No") 
      
# # This code is contributed by Ansh Riyal 
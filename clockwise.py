import math
import re

# pts = [
#     [49, 49], [52, 64], [20, 26], [40, 30], [21, 47], [17, 63], [31, 62], [52, 33], [51, 21], [42, 41],
#     [31, 32], [5, 25], [12, 42], [36, 16], [52, 41], [27, 23], [17, 33], [13, 13], [57, 58], [62, 42], [42, 57],
#     [16, 57], [8, 52], [7, 38], [27, 68], [30, 48], [43, 67], [58, 48], [58, 27], [37, 69], [38, 46], [46, 10], [61, 33],
#     [62, 63], [63, 69], [32, 22], [45, 35], [59, 15], [5, 6], [10, 17], [21, 10], [5, 64], [30, 15], [39, 10], [32, 39],
#     [25, 32], [25, 55], [48, 28], [56, 37], [30, 40]]
def clockwise(path):
    with open(path, "r") as f:
        data = f.read()
        pts = re.findall(r'\d{1,3} (\d{1,3} \d{1,3})\n', data)
        
    def str_to_list(s):
        return [float(x) for x in s.split()]

    pts = [str_to_list(x) for x in pts]
    origin = pts[0]  # poczatek
    refvec = [-1, -1]  # wskazowka zegara

    def clockwiseangle_and_distance(point):
        # Vector between point and the origin: v = p - o
        vector = [point[0]-origin[0], point[1]-origin[1]]
        # Length of vector: ||v||
        lenvector = math.hypot(vector[0], vector[1])
        # If length is zero there is no angle
        if lenvector == 0:
            return -math.pi, 0
        # Normalize vector: v/||v||
        normalized = [vector[0]/lenvector, vector[1]/lenvector]
        dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
        diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
        angle = math.atan2(diffprod, dotprod)
        # Negative angles represent counter-clockwise angles so we need to subtract them 
        # from 2*pi (360 degrees)
        if angle < 0:
            return 2*math.pi+angle, lenvector
        # I return first the angle because that's the primary sorting criterium
        # but if two vectors have the same angle then the shorter distance should come first.
        return angle, lenvector

    done = sorted(pts[1:], key=clockwiseangle_and_distance)
    return done

# done = clockwise()
    # print(done)
    # import matplotlib.pyplot as plt

    # x_val = [x[0] for x in done]
    # y_val = [y[1] for y in done]
    # plt.scatter(x_val, y_val)
    # plt.scatter(origin[0], origin[1], marker="*")
    # plt.plot(x_val, y_val)
    # plt.show()
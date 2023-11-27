import math 
import numpy as np

def euclidean_distance(vec_1, vec_2):
    #a = np.array([1,2,3,4])
    #b = np.array([5,6,7,8])

    dist = 0
    for x, y in zip(vec_1, vec_2):
        dist += (x - y) ** 2
    return math.sqrt(dist)